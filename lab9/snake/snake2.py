import pygame
import sys
import random
import time

pygame.init()

# настройк экрана
width, height = 500, 500
cell_size = 10
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Цвет
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
gold = (255, 215, 0)
blue = (50, 153, 213)
white = (255, 255, 255)

# Параметры змейки
snake_pos = [100, 100]  # Начальная позиция головы змейки
snake_body = [[100, 100], [90, 100], [80, 100]]  # Тело змейки
direction = "RIGHT"
change_to = direction

# начальные параметры игры
score = 0
level = 1
speed = 10  # Нчальная скорость игры
food_eaten = 0  # счётчик съеденных яблок пон
level_up_eaten = 4  # Уровень увеличивается после 4 яблок

# фпс и шрифты
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 25)
score_font = pygame.font.SysFont("Verdana", 35)

# лист с едой
foods = []


# еда
class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = random.randrange(0, width - cell_size, cell_size)
        self.y = random.randrange(0, height - cell_size, cell_size)
        self.weight = random.choices([10, 30], weights=[0.8, 0.2])[0]
        self.color = red if self.weight == 10 else gold
        self.created_time = time.time()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, cell_size, cell_size))

    def is_expired(self, timeout=6):
        return time.time() - self.created_time > timeout


# функция для отображения счёта и уровня
def show_score(score, level):
    value = score_font.render(f"Score: {score}  Level: {level}", True, black)
    screen.blit(value, [0, 450])


# функция для отрисовки змейки
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(
            screen, green, pygame.Rect(block[0], block[1], snake_block, snake_block)
        )


# функция для генерации еды, чтобы она не пересекалась с телом змейки
def generate_food():
    while True:
        food = Food()
        if [food.x, food.y] not in snake_body:
            foods.clear()  # Проверка, чтобы еда не появлялась на теле змейки
            foods.append(food)
            break


generate_food()

# игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    direction = change_to

    # Обновляем позицию головы змейки в зависимости от направления
    if direction == "UP":
        snake_pos[1] -= cell_size
    elif direction == "DOWN":
        snake_pos[1] += cell_size
    elif direction == "LEFT":
        snake_pos[0] -= cell_size
    elif direction == "RIGHT":
        snake_pos[0] += cell_size

    # Проверка на столкновение с границей экрана
    if (
        snake_pos[0] < 0
        or snake_pos[0] >= width
        or snake_pos[1] < 0
        or snake_pos[1] >= height
    ):
        running = False  # Игра заканчивается, если змейка вышла за пределы ;(

    # Добавляем новую голову змейки
    snake_body.insert(0, list(snake_pos))

    # чекаем если съела яблоко
    eaten = False
    for food in foods[:]:
        if snake_pos == [food.x, food.y]:
            score += food.weight  # увеличиваем счёт
            food_eaten += 1  # увеличиваем счётчик съеденной еды
            foods.remove(food)
            generate_food()  # Генерируем новую еду
            eaten = True
            if food_eaten >= level_up_eaten:
                level += 1
                speed += 2
                food_eaten = 0
            break

    if not eaten:
        snake_body.pop()  # Убираем последний хвост, если змейка не съела еду

    for food in foods[:]:
        if food.is_expired():
            foods.remove(food)
            generate_food()

    # Отображаем экран
    screen.fill(white)
    pygame.draw.rect(screen, white, (0, 0, width, height))  # HUD
    draw_snake(cell_size, snake_body)
    for food in foods:
        food.draw()
    show_score(score, level)

    pygame.display.flip()
    clock.tick(speed)  # fps

# Завершаем игру
pygame.quit()
sys.exit()
