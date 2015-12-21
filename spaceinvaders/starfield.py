import pygame
import random

from spaceinvaders.utils import Vec2

STAR_SIZE = Vec2(2, 2)

stars = []

screen_info = pygame.display.Info()

for i in range(0, 250):
    x = random.randrange(0, screen_info.current_w - STAR_SIZE.x)
    y = random.randrange(0, screen_info.current_h - STAR_SIZE.y)
    stars.append(pygame.Rect(x, y, STAR_SIZE.x, STAR_SIZE.y))

def draw(screen):
    for star in stars:
        pygame.draw.rect(screen, (255, 255, 255), star)
