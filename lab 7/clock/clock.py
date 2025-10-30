import pygame
import time
import math

pygame.init()

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()


pygame.display.set_caption("Мики Маус Часы")

chasiki = pygame.image.load('C:\\Users\\ramaz\\Desktop\\lab 7\\clock\\chasi.png')
levo = pygame.image.load('C:\\Users\\ramaz\\Desktop\\lab 7\\clock\\levo.png')
pravo = pygame.image.load('C:\\Users\\ramaz\\Desktop\\lab 7\\clock\\pravo.png')

chasiki = pygame.transform.scale(chasiki, (1000, 800))
pravo=pygame.transform.scale(pravo, (1000, 800))
levo=pygame.transform.scale(levo, (40, 800))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current = time.localtime()


    minute = current.tm_min
    second = current.tm_sec

    secondAngle = -second * 6
    minuteAngle = -minute * 6 - (second / 60) * 6 - 50

    screen.blit(chasiki, (0, 0))

    rotatedPravo = pygame.transform.rotate(pravo, minuteAngle)
    
    pravoRect = rotatedPravo.get_rect(center=(500, 400))
    screen.blit(rotatedPravo, pravoRect)

    rotatedLevo = pygame.transform.rotate(levo, secondAngle)
    
    levoRect = rotatedLevo.get_rect(center=(500, 400))
    screen.blit(rotatedLevo, levoRect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

