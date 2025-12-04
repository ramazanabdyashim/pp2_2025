import psycopg2
import csv


def connect_db():
    """Устанавливает соединение с базой данных"""
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="252566",
        host="localhost",
        client_encoding="utf-8"
    )


def validate_phone(phone):
    """Проверяет корректность номера телефона"""
    return phone.isdigit() and 10 <= len(phone) <= 15


def search_by_pattern():
    """Поиск записей по шаблону"""
    conn = connect_db()
    cursor = conn.cursor()
    pattern = input("Введите строку для поиска: ")

    cursor.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    results = cursor.fetchall()

    if not results:
        print("Записи не найдены")
    else:
        print("\nРезультаты поиска:")
        print("{:<5} {:<15} {:<15} {:<15}".format("ID", "Имя", "Фамилия", "Телефон"))
        print("-" * 50)
        for row in results:
            print("{:<5} {:<15} {:<15} {:<15}".format(*row))

    cursor.close()
    conn.close()


def update_user():
    """Добавление или обновление пользователя"""
    conn = connect_db()
    cursor = conn.cursor()

    print("\nДобавление/обновление пользователя")
    first_name = input("Имя: ").strip()
    last_name = input("Фамилия: ").strip()
    phone = input("Телефон: ").strip()

    if not validate_phone(phone):
        print("Ошибка: Некорректный номер телефона (должен содержать 10-15 цифр)")
        return

    # Исправленный вызов процедуры
    cursor.execute(
        "CALL update_user(%s::VARCHAR(50), %s::VARCHAR(50), %s::VARCHAR(15))",
        (first_name, last_name, phone)
    )

    conn.commit()
    print("Операция выполнена успешно!")
    cursor.close()
    conn.close()


def insert_many_users():
    """Массовое добавление пользователей"""
    conn = connect_db()
    cursor = conn.cursor()

    users = []
    print("\nВведите данные (имя,фамилия,телефон). Для завершения введите 'done':")

    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'done':
            break

        parts = user_input.split(',')
        if len(parts) != 3:
            print("Используйте: имя,фамилия,телефон")
            continue

        users.append([parts[0].strip(), parts[1].strip(), parts[2].strip()])

    if not users:
        print("Не введено ни одного пользователя")
        return

    # Формируем массив для PostgreSQL
    users_str = "ARRAY["
    users_str += ",".join([f"ARRAY['{u[0]}','{u[1]}','{u[2]}']" for u in users])
    users_str += "]::TEXT[][]"

    # Вызываем процедуру и получаем некорректные данные
    cursor.execute(f"""
    DO $$
    DECLARE
        incorrect TEXT[];
    BEGIN
        CALL insert_many_users({users_str}, incorrect);
        RAISE NOTICE 'Некорректные данные: %', incorrect;
    END $$;
    """)
    conn.commit()

    print("\nГотово!")
    cursor.close()
    conn.close()


def paginated():
    """Получение записей с пагинацией"""
    conn = connect_db()
    cursor = conn.cursor()

    limit = input("Количество записей на странице: ")
    offset = input("Смещение: ")

    if not limit.isdigit() or not offset.isdigit():
        print("Ошибка: введите числа для limit и offset")
        return

    cursor.execute("SELECT * FROM paginated(%s, %s)", (int(limit), int(offset)))
    results = cursor.fetchall()

    if not results:
        print("Записи не найдены")
    else:
        print("\nРезультаты:")
        print("{:<5} {:<15} {:<15} {:<15}".format("ID", "Имя", "Фамилия", "Телефон"))
        print("-" * 50)
        for row in results:
            print("{:<5} {:<15} {:<15} {:<15}".format(*row))

    cursor.close()
    conn.close()


def delete_by_username_or_phone():
    """Удаление записей по имени или телефону"""
    conn = connect_db()
    cursor = conn.cursor()

    search_term = input("Введите имя, фамилию или часть номера телефона для удаления: ")

    cursor.execute("CALL delete_by_username_or_phone(%s)", (search_term,))
    conn.commit()

    print(f"Удалено записей: {cursor.rowcount}")
    cursor.close()
    conn.close()


def main():
    """Главное меню"""
    print("Система управления телефонной книгой")

    while True:
        print("\nМеню:")
        print("1. Поиск по шаблону")
        print("2. Добавить/обновить пользователя")
        print("3. Массовое добавление пользователей")
        print("4. Просмотр с пагинацией")
        print("5. Удаление по имени/телефону")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()


        if choice == "1":
            search_by_pattern()
        elif choice == "2":
            update_user()
        elif choice == "3":
            insert_many_users()
        elif choice == "4":
            paginated()
        elif choice == "5":
            delete_by_username_or_phone()
        elif choice == "0":
            print("Выход из системы")
            break
        else:
            print("Неверный выбор, попробуйте снова")


if __name__ == "__main__":
    main()
