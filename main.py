import pygame
from time import sleep


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FIELD_WIDTH = 110
FIELD_HEIGHT = 50

PINK = (255, 20, 147)
GREEN = (0, 255, 0)

pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Put your header here")
clock = pygame.time.Clock()

for i in range(WINDOW_HEIGHT - FIELD_HEIGHT):
    clock.tick(50)
    surface.fill(PINK)
    top = i**2 / 2
    if top + FIELD_HEIGHT > WINDOW_HEIGHT:
        top = WINDOW_HEIGHT - FIELD_HEIGHT
    rect = pygame.Rect((WINDOW_WIDTH - FIELD_WIDTH) / 2, top, 110, 55)
    pygame.draw.rect(surface, GREEN, rect)
    pygame.display.update()
sleep(1)
pygame.quit()
