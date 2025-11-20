import pygame
import sys
import math

# Initialize pygame
pygame.init()

# настройки поверхности
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

# настройки цвета
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# настройи кисточки
drawing = False
brush_color = black
shape = "brush"
last_pos = None


# класс с кнопками
class Button:
    def __init__(self, x, y, width, height, text, color, action):

        # Инициализировать кнопку с позицией, размером, текстом, цветом и действием

        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):

        # Нарисовать кнопку на экране

        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 6))

    def check_action(self, event):

        # Проверить, была ли нажата кнопка, и выполнить ее действие

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()


# функции для выбора цветаа и фигру
def set_black():
    # Выбрать черный цвет кисти
    global brush_color
    brush_color = black


def set_green():
    # Выбрать зеленый цвет кисти
    global brush_color
    brush_color = green


def set_red():
    # Выбрать красный цвет кисти
    global brush_color
    brush_color = red


def set_blue():
    # Выбрать синий цвет кисти
    global brush_color
    brush_color = blue


def set_rectangle():
    # Выбрать инструмент прямоугольник
    global shape
    shape = "rectangle"


def set_square():
    # Выбрать инструмент квадрат
    global shape
    shape = "square"


def set_circle():
    # Выбрать инструмент круг
    global shape
    shape = "circle"


def set_right_triangle():
    # Выбрать инструмент прямоугольный треугольник
    global shape
    shape = "right_triangle"


def set_equilateral_triangle():
    # Выбрать инструмент равносторонний треугольник
    global shape
    shape = "equilateral_triangle"


def set_rhombus():
    # Выбрать инструмент ромб
    global shape
    shape = "rhombus"


def set_brush():
    # Выбрать инструмент кисть
    global shape
    shape = "brush"


def set_eraser():
    # Выбрать инструмент ластик
    global shape
    shape = "eraser"


def clear_screen():
    screen.fill(white)


def exit_app():
    # Выход из приложения
    pygame.quit()
    sys.exit()


# положение кнопок
buttons = [
    Button(10, 10, 100, 30, "Red", black, set_red),
    Button(10, 50, 100, 30, "Green", black, set_green),
    Button(10, 90, 100, 30, "Blue", black, set_blue),
    Button(10, 130, 100, 30, "Black", black, set_black),
    Button(10, 170, 100, 30, "Rectangle", black, set_rectangle),
    Button(10, 210, 100, 30, "Square", black, set_square),
    Button(10, 250, 100, 30, "Circle", black, set_circle),
    Button(10, 290, 100, 30, "R Triangle", black, set_right_triangle),
    Button(10, 330, 100, 30, "E Triangle", black, set_equilateral_triangle),
    Button(10, 370, 100, 30, "Rhombus", black, set_rhombus),
    Button(10, 410, 100, 30, "Brush", black, set_brush),
    Button(10, 450, 100, 30, "Eraser", black, set_eraser),
    Button(10, 490, 100, 30, "Clear", black, clear_screen),
    Button(10, 530, 100, 30, "Exit", black, exit_app),
]


# клир сделать
clear_screen()

# Main loop
clock = pygame.time.Clock()
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = pygame.mouse.get_pos()  # старт для непрерывной линии

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None

        for button in buttons:
            button.check_action(event)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if drawing and mouse_y > 60:
        current_pos = (mouse_x, mouse_y)

        if shape == "brush":
            if last_pos is not None:
                pygame.draw.line(screen, brush_color, last_pos, current_pos, 10)
            last_pos = current_pos

        elif shape == "rectangle":
            pygame.draw.rect(
                screen,
                brush_color,
                pygame.Rect(mouse_x - 50, mouse_y - 50, 150, 100),
                2,
            )

        # Square tool draws 80x80 square
        elif shape == "square":
            pygame.draw.rect(
                screen,
                brush_color,
                pygame.Rect(mouse_x - 40, mouse_y - 40, 80, 80),
                2,
            )

        elif shape == "circle":
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 50, 2)

        elif shape == "right_triangle":

            points = [
                (mouse_x - 50, mouse_y + 50),
                (mouse_x + 50, mouse_y + 50),
                (mouse_x - 50, mouse_y - 50),
            ]
            pygame.draw.polygon(screen, brush_color, points, 2)

        elif shape == "equilateral_triangle":

            side_length = 80
            height = side_length * math.sqrt(3) / 2

            points = [
                (mouse_x, mouse_y - height / 2),
                (mouse_x - side_length / 2, mouse_y + height / 2),
                (mouse_x + side_length / 2, mouse_y + height / 2),
            ]
            pygame.draw.polygon(screen, brush_color, points, 2)

        elif shape == "rhombus":

            points = [
                (mouse_x, mouse_y - 50),
                (mouse_x + 40, mouse_y),
                (mouse_x, mouse_y + 50),
                (mouse_x - 40, mouse_y),
            ]
            pygame.draw.polygon(screen, brush_color, points, 2)

        elif shape == "eraser":
            if last_pos is not None:
                pygame.draw.line(screen, white, last_pos, current_pos, 20)
            last_pos = current_pos
    else:

        last_pos = None

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

    clock.tick(60)
