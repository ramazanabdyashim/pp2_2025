import psycopg2
import csv

def connect_db():
    try:
        return psycopg2.connect(
            host="localhost",
            database="postgres", 
            user="postgres",
            password="252566",  
            port="5432"
        )
    except Exception as err:
        print(f"Ошибка подключения: {err}")
        return None

def create_table():
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone_number VARCHAR(20) UNIQUE
            )
        """)
        conn.commit()
        print("Таблица 'phonebook' создана!")
        
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        tables = cur.fetchall()
        print("Таблицы в базе:", [table[0] for table in tables])
        
    except Exception as err:
        print(f"Ошибка: {err}")
    finally:
        cur.close()
        conn.close()


def load_from_csv():
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        
        with open('example.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (row['first_name'], row['last_name'], row['phone_number'])
                )
        
        conn.commit()
        print("Готово!")
        
        cur.execute("SELECT * FROM phonebook")
        print("\nКонтакты в базе:")
            
    except Exception as err:
        print(f"Ошибка: {err}")
    finally:
        cur.close()
        conn.close()

def add_manual():
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (name, last_name, phone)
        )
        conn.commit()
        print("Контакт добавлен!")
        
    except Exception as err:
        print(f"Ошибка: {err}")
    finally:
        cur.close()
        conn.close()

def search_contacts():
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook")
        contacts = cur.fetchall()
        
        print("\n Все контакты:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Имя: {contact[1]}, Фамилия: {contact[2]}, Телефон: {contact[3]}")
            
    except Exception as err:
        print(f"Ошибка: {err}")
    finally:
        cur.close()
        conn.close()

def update_contact():
    phone = input("Введите телефон для изменения: ")
    new_name = input("Введите новое имя: ")
    
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE phonebook SET first_name = %s WHERE phone_number = %s",
            (new_name, phone)
        )
        conn.commit()
        print("Готово!")
        
    except Exception as err:
        print(f"Ошибка: {err   }")
    finally:
        cur.close()
        conn.close()

def delete_contact():
    phone = input("Введите телефон для удаления: ")
    
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
        conn.commit()
        print("Готово")
        
    except Exception as err:
        print(f"Ошибка: {err}")
    finally:
        cur.close()
        conn.close()

def main():
    print("----PhoneBook----")
    
    create_table()
    
    while True:
        print("\"nЧто вы хотите сделать?")
        print("1 - Загрузить данные из файла")
        print("2 - Добавить контакт через консоль")
        print("3 - Показать все контакты")
        print("4 - Обновить контакт")
        print("5 - Удалить контакт")
        print("0 - Выход")
        
        choice = input("Выбрать: ")
        
        if choice == "1":
            load_from_csv()
        elif choice == "2":
            add_manual()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()