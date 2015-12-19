import pygame
import sys

# Initialize
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

from spaceinvaders import assets, entities, events

# Set up window
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.transform.scale(assets.IMAGES['alien'], (32, 32)))

clock = pygame.time.Clock()
score = 0

# Game objects
player = entities.Player(200, screen.get_rect().height - 50)
enemy_waves = [events.spawn_wave(200, 0)]

# Game loop
while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			sys.exit()
		elif ev.type == pygame.KEYDOWN:
			events.keyboard_callback(ev.key, player = player, waves = enemy_waves)
		else:
			continue
			
	delta = clock.tick(60) / 1000 # as seconds
	
	screen.fill((0, 0, 0))
	
	player.update(delta)
	player.draw(screen)
	
	for wave in enemy_waves:
		wave.update(delta)
		wave.draw(screen)
		
		# Shoot down ze aliens
		for alien in wave:
			for shot in player.shot_group:
				if alien.rect.contains(shot.rect):
					alien.kill()
					shot.kill()
					score += 10
		
	text = assets.FONTS['main'].render('Score: {0}'.format(score), False, (255, 255, 255))
	screen.blit(text, text.get_rect())
	
	pygame.display.flip()