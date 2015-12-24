import pygame
import os

# Base directory containing game assets.
ASSETS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

IMAGES = {
	'alien' : pygame.image.load(os.path.join(ASSETS_DIR, 'Space_Invaders_Alien.png')),
	'player_ship' : pygame.image.load(os.path.join(ASSETS_DIR, 'spaceship.png')),
	'laser_red' : pygame.image.load(os.path.join(ASSETS_DIR, 'laser_red.png')),
}

AUDIO = {
	'laser1' : pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'laser1.wav')),
	'laser2' : pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'laser2.wav')),
}

FONTS = {
	'main' : pygame.font.Font(os.path.join(ASSETS_DIR, 'Munro.ttf'), 32),
}
