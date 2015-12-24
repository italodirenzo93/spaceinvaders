import pygame

from spaceinvaders import assets
from spaceinvaders.entities import Sprite
from spaceinvaders.utils import Vec2

screen_info = pygame.display.Info()

MOVE_SPEED = 250

player_sprite = Sprite(assets.IMAGES['player_ship'], screen_info.current_w / 2, screen_info.current_h - 50, 18, 18, 36, 36)
shot_group = pygame.sprite.RenderPlain()

def fire_shot():
	position = player_sprite.get_position()
	shot = Sprite(assets.IMAGES['laser_red'], position.x, position.y, 5, 15, 10, 30)
	shot_group.add(shot)

def update(delta):
	keys_down = pygame.key.get_pressed()
		
	if keys_down[pygame.K_LEFT]:
		player_sprite.move(-MOVE_SPEED * delta, 0)
	if keys_down[pygame.K_RIGHT]:
		player_sprite.move(MOVE_SPEED * delta, 0)
		
	# Detect screen bounds
	if player_sprite.rect.x <= 0:
		player_sprite.rect.x = 0
	if player_sprite.rect.x + player_sprite.rect.width >= screen_info.current_w:
		player_sprite.rect.x = screen_info.current_w - player_sprite.rect.width
		
	# Fire shots
	for shot in shot_group:
		shot.move(0, -600 * delta)
		if shot.get_position().y < 0:
			shot.kill()
	
def draw(screen):
	shot_group.draw(screen)
	player_sprite.draw(screen)
