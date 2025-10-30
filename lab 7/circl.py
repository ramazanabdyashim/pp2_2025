import pygame
import sys

pygame.init()



screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Красный мящик")

ball_radius = 228
ball_x = 1000 // 2
ball_y = 800 // 2

speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < 1000:
        ball_x += speed
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < 800:
        ball_y += speed

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255,0,0), (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
