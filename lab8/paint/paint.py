import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# Brush settings
drawing = False
brush_color = black
shape = "brush"  # default is freeform brush
last_pos = None  # для непрерывной линии


# Button class to create and manage buttons
class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 6))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()


# Functions for color and shape selection
def set_black():
    global brush_color
    brush_color = black


def set_green():
    global brush_color
    brush_color = green


def set_red():
    global brush_color
    brush_color = red


def set_blue():
    global brush_color
    brush_color = blue


def set_rectangle():
    global shape
    shape = "rectangle"


def set_circle():
    global shape
    shape = "circle"


def set_brush():
    global shape
    shape = "brush"


def set_eraser():
    global shape
    shape = "eraser"


def clear_screen():
    screen.fill(white)


def exit_app():
    pygame.quit()
    sys.exit()


# Buttons setup
buttons = [
    Button(10, 10, 70, 30, "Black", black, set_black),
    Button(80, 10, 70, 30, "Green", green, set_green),
    Button(150, 10, 70, 30, "Red", red, set_red),
    Button(220, 10, 70, 30, "Blue", blue, set_blue),
    Button(290, 10, 100, 30, "Rectangle", gray, set_rectangle),
    Button(390, 10, 70, 30, "Circle", gray, set_circle),
    Button(460, 10, 70, 30, "Brush", gray, set_brush),
    Button(530, 10, 70, 30, "Eraser", gray, set_eraser),
    Button(600, 10, 70, 30, "Clear", gray, clear_screen),
    Button(670, 10, 70, 30, "Exit", gray, exit_app),
]

# Initialize the screen
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
                last_pos = None  # сброс цепочки линии

        for button in buttons:
            button.check_action(event)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if drawing and mouse_y > 60:
        current_pos = (mouse_x, mouse_y)

        if shape == "brush":
            # непрерывная линия кистью
            if last_pos is not None:
                pygame.draw.line(
                    screen, brush_color, last_pos, current_pos, 10
                )  # толщина 10
            last_pos = current_pos

        elif shape == "rectangle":
            pygame.draw.rect(
                screen,
                brush_color,
                pygame.Rect(mouse_x - 50, mouse_y - 50, 100, 100),
                2,
            )

        elif shape == "circle":
            pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), 50, 2)

        elif shape == "eraser":
            # непрерывная «полоса» ластика
            if last_pos is not None:
                pygame.draw.line(
                    screen, white, last_pos, current_pos, 20
                )  # ластик потолще
            last_pos = current_pos
    else:
        # вне рисования или над панелью — сбрасываем, чтобы не было «скачков»
        last_pos = None

    # Draw the toolbar with buttons (поверх холста)
    pygame.draw.rect(screen, gray, (0, 0, width, 50))  # toolbar background
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)
