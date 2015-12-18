import pygame
import sys
from spaceinvaders import assets
from spaceinvaders import entities

# Events
def keyboard_callback(keycode, **kwargs):
	if keycode == pygame.K_ESCAPE:
		sys.exit()
	elif keycode == pygame.K_SPACE:
		player = kwargs['player']
		player.shot_manager.fire_shot(player.rect.x + player.rect.width/2, player.rect.y + player.rect.height/2)
	else:
		return

def spawn_wave(pos_x, pos_y):
	"""
	Spawns a wave of enemies in a 5x3 pattern.
	Returns: A new AlienGroup containing the wave of enemies.
	"""			
	group = entities.AlienGroup()
	for y in range(0, 3):
		for x in range(0, 5):
			a = entities.Alien()
			a.set_position(pos_x + (a.rect.width * x), pos_y + (a.rect.height * y))
			group.add(a)
	return group