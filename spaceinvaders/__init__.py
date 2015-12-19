import pygame
import sys

# Globals
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

score = 0

# Initialize
pygame.init()
pygame.font.init()

from spaceinvaders import assets, entities, events

def start_game():
	"""
	Begins the game
	"""
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
	pygame.display.set_caption('Space Invaders')
	pygame.display.set_icon(pygame.transform.scale(assets.IMAGES['alien'], (32, 32)))

	clock = pygame.time.Clock()

	# Game objects
	player = entities.Player(200, screen.get_rect().height - 50)
	enemy_waves = [events.spawn_wave(200, 0)]

	# Game loop
	while True:
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				sys.exit()
			elif ev.type == pygame.KEYDOWN:
				events.keyboard_callback(ev.key, player=player)
			else:
				continue
				
		delta = clock.tick(60) / 1000 # as seconds
		
		screen.fill((0, 0, 0))
		
		player.update(delta)
		player.draw(screen)
		
		for wave in enemy_waves:
			wave.update(delta)
			wave.draw(screen)
			
		text = assets.FONTS['main'].render('Score: {0}'.format(score), False, (255, 255, 255))
		screen.blit(text, text.get_rect())
		
		pygame.display.flip()