import pygame
import sys
import random

# Initialize
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

video_settings = {
	'res' : (800, 600),
	'flags' : pygame.HWSURFACE | pygame.DOUBLEBUF
}

# Parse command line
if len(sys.argv) > 1:
	if sys.argv[1] == '-f':
		video_settings['flags'] |= pygame.FULLSCREEN
		screen_info = pygame.display.Info()
		video_settings['res'] = (screen_info.current_w, screen_info.current_h)

# Set up window
screen = pygame.display.set_mode(video_settings['res'], video_settings['flags'])

from spaceinvaders import assets, entities, events

pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.transform.scale(assets.IMAGES['alien'], (32, 32)))
pygame.mouse.set_visible(False)

# Game objects
from spaceinvaders import globals
from spaceinvaders import starfield, player

ENEMY_SPAWN_CHANCE = 0.002

# Game loop
while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			sys.exit()
		elif ev.type == pygame.KEYDOWN:
			events.keyboard_callback(ev.key)
		else:
			continue
			
	delta = globals.clock.tick(60) / 1000.0 # as seconds
	
	# Updates
	if not globals.is_paused:
		starfield.update(delta)
		player.update(delta)
		
		if random.random() < ENEMY_SPAWN_CHANCE:
			globals.enemy_waves.append(events.spawn_wave(random.randrange(screen.get_rect().width - 300), 0))
		
		for wave in globals.enemy_waves:
			wave.update(delta)
			if len(pygame.sprite.groupcollide(player.shot_group, wave, True, True)) > 0:
				globals.score += 10
			
			for enemy in wave:
				if events.is_colliding(player.player_sprite, enemy) or enemy.get_position().y > screen.get_rect().height:
					player.dead = True
	
	# Draws
	screen.fill((0, 0, 0))
	
	starfield.draw(screen)
	player.draw(screen)
	
	for wave in globals.enemy_waves:
		wave.draw(screen)
		
	text = assets.FONTS['main'].render('Score: {0}'.format(globals.score), False, (255, 255, 255))
	screen.blit(text, text.get_rect())
	
	if player.dead:
		gameover_text = assets.FONTS['main'].render('GAME OVER', False, (255, 255, 255))
		gameover_dst = gameover_text.get_rect()
		gameover_dst.x = screen.get_rect().width / 2 - gameover_dst.width / 2
		gameover_dst.y = screen.get_rect().height / 2 - gameover_dst.height / 2
		screen.blit(gameover_text, gameover_dst)
	
	if globals.is_paused:
		pause_text = assets.FONTS['main'].render('PAUSED', False, (255, 255, 255))
		pause_dst = pause_text.get_rect()
		pause_dst.x = screen.get_rect().width / 2 - pause_dst.width / 2
		pause_dst.y = screen.get_rect().height / 2 - pause_dst.height / 2
		screen.blit(pause_text, pause_dst)
	
	# Draw buffer to screen
	pygame.display.flip()
