import pygame
import random

from spaceinvaders.utils import Vec2

STAR_COUNT = 250
STAR_SIZE = Vec2(2, 2)
STAR_SPEED = 70

stars = []

screen_info = pygame.display.Info()

for i in range(0, STAR_COUNT):
    x = random.randrange(0, screen_info.current_w - STAR_SIZE.x)
    y = random.randrange(0, screen_info.current_h - STAR_SIZE.y)
    stars.append(pygame.Rect(x, y, STAR_SIZE.x, STAR_SIZE.y))
    
def update(delta):
	for star in stars:
		star.y += STAR_SPEED * delta
		if star.y > screen_info.current_h:
			stars.remove(star)
			stars.append(pygame.Rect(random.randrange(0, screen_info.current_w - STAR_SIZE.x), 0, STAR_SIZE.x, STAR_SIZE.y))

def draw(screen):
    for star in stars:
        pygame.draw.rect(screen, (255, 255, 255), star)
