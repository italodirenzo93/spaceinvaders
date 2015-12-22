import pygame
import sys

# Initialize
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

from spaceinvaders import assets, entities, events

# Set up window
screen = pygame.display.set_mode((1024, 720), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.transform.scale(assets.IMAGES['alien'], (32, 32)))

clock = pygame.time.Clock()
score = 0

# Game objects
from spaceinvaders import starfield, player
enemy_waves = [events.spawn_wave(screen.get_rect().width / 2, 0)]

# Game loop
while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			sys.exit()
		elif ev.type == pygame.KEYDOWN:
			events.keyboard_callback(ev.key, player = player, waves = enemy_waves)
		else:
			continue
			
	delta = clock.tick(60) / 1000.0 # as seconds
	
	screen.fill((0, 0, 0))
	
	starfield.update(delta)
	starfield.draw(screen)
	
	player.update(delta)
	player.draw(screen)
	
	for wave in enemy_waves:
		wave.update(delta)
		wave.draw(screen)
		if len(pygame.sprite.groupcollide(player.shot_group, wave, True, True)) > 0:
			score += 10
		
	text = assets.FONTS['main'].render('Score: {0}'.format(score), False, (255, 255, 255))
	screen.blit(text, text.get_rect())
	
	pygame.display.flip()
