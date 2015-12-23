import pygame
import sys

from spaceinvaders import assets, entities, globals, player
from spaceinvaders.utils import Vec2

# Events
def spawn_wave(pos_x, pos_y):
	"""
	Spawns a wave of enemies in a 5x3 pattern.
	Returns: A new AlienGroup containing the wave of enemies.
	"""	
	group = entities.AlienGroup()
	scale_factor = Vec2(48, 48)
	
	for y in range(0, 3):
		for x in range(0, 5):
			alien = entities.Sprite(
				assets.IMAGES['alien'],
				pos_x + (scale_factor.x * x),
				pos_y + (scale_factor.y * y),
				0, 0,
				scale_factor.x, scale_factor.y)
			group.add(alien)
			
	return group

def keyboard_callback(keycode):
	if keycode == pygame.K_SPACE:
		if not globals.is_paused:
			player.fire_shot()
			assets.AUDIO['laser1'].play()
	elif keycode == pygame.K_i:
		globals.enemy_waves.append(spawn_wave(200, 0))
	elif keycode == pygame.K_RETURN:
		globals.is_paused = not globals.is_paused
	else:
		return
