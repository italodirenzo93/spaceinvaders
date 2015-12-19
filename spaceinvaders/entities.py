import pygame
import random

from spaceinvaders import assets
from spaceinvaders.utils import Vec2
	
# Classes
class Sprite(pygame.sprite.Sprite):
	def __init__(self, image, tag, x = 0, y = 0, origin_x = 0, origin_y = 0, scale_x = 0, scale_y = 0):
		super().__init__()
		
		self.tag = tag
		self.scale = Vec2(scale_x, scale_y)
		self.origin = Vec2(origin_x, origin_y)
		
		self.image = pygame.transform.scale(image, (self.scale.x, self.scale.y))
		self.rect = self.image.get_rect()
		self.rect.x = x - self.origin.x
		self.rect.y = y - self.origin.y
		
	def get_position(self):
		return Vec2(self.rect.x + self.origin.x, self.rect.y + self.origin.y)
		
	def set_position(self, x, y):
		self.rect.x = x - self.origin.x
		self.rect.y = y - self.origin.y
	
	def move(self, x, y):
		self.rect.x += x
		self.rect.y += y
	
	# Override
	def update(self, delta):
		pass
		
	def draw(self, screen):
		screen.blit(self.image, self.rect)


class Player(Sprite):
	"""
	Controls gameplay logic of the player spaceship.
	"""
	# Constructor
	def __init__(self, x, y):
		super().__init__(assets.IMAGES['player_ship'], 'player', x, y, 18, 18, 36, 36)
		self.move_speed = 250
		self.shot_group = pygame.sprite.Group()
		
	def fire_shot(self):
		position = self.get_position()
		shot = Sprite(assets.IMAGES['laser_red'], 'laser_player', position.x, position.y, 5, 15, 10, 30)
		self.shot_group.add(shot)
	
	# Override
	def update(self, delta):
		keys_down = pygame.key.get_pressed()
		
		if keys_down[pygame.K_LEFT]:
			self.rect.x -= self.move_speed * delta
		if keys_down[pygame.K_RIGHT]:
			self.rect.x += self.move_speed * delta
			
		# Detect screen bounds
		screen_info = pygame.display.Info()
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x + self.rect.width >= screen_info.current_w:
			self.rect.x = screen_info.current_w - self.rect.width
			
		# Fire shots
		for shot in self.shot_group:
			shot.move(0, -600 * delta)
			if shot.get_position().y < 0:
				shot.kill()
	
	def draw(self, screen):
		for shot in self.shot_group:
			shot.draw(screen)
		super().draw(screen)


class AlienGroup(pygame.sprite.Group):
	"""
	Custom group for holding alien objects.
	Overrides update method in order to update all sprites
	in unison rather than individually.
	"""
	# Constructor
	def __init__(self, *sprites):
		super().__init__(*sprites)
		self.wait_time = 0
		
	# Override
	def update(self, delta):
		self.wait_time += delta
		
		if self.wait_time >= 2:	# move every 2 seconds
			direction_chance = random.randrange(0, 20)
			
			for alien in self:
				if direction_chance in range(0, 2):
					alien.set_position(alien.rect.x - alien.rect.width / 2, alien.rect.y)
				elif direction_chance in range(3, 5):
					alien.set_position(alien.rect.x + alien.rect.width / 2, alien.rect.y)
				else:
					alien.set_position(alien.rect.x, alien.rect.y + alien.rect.height / 2)
				
			self.wait_time = 0