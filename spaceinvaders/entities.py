import pygame
import random

from spaceinvaders import assets, SCREEN_WIDTH
		
# Classes
class Shot(pygame.sprite.Sprite):
	def __init__(self, x = 0, y = 0):
		super().__init__()
		self.image = pygame.transform.scale(assets.IMAGES['laser_red'], (10, 30))
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x - self.rect.width/2, y - self.rect.height/2
	
	def get_center(self):
		return (self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2)

class ShotManager(object):
	shot_group = pygame.sprite.Group()
	
	def fire_shot(self, x, y):
		s = Shot(x, y)
		self.shot_group.add(s)
		
	def update(self, delta):
		for shot in self.shot_group:
			shot.rect.y -= 600 * delta
			if shot.rect.y + shot.rect.height < 0:
				shot.kill()
				print('Shot destroyed')

	def draw(self, screen):
		self.shot_group.draw(screen)

class Player(pygame.sprite.Sprite):
	"""
	Controls gameplay logic of the player spaceship.
	"""
	# Constructor
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.transform.scale(assets.IMAGES['player_ship'], (36, 36))
		self.rect = self.image.get_rect()
		# Set origin point to center
		self.rect.x, self.rect.y = x - self.rect.width/2, y - self.rect.height/2
		
		self.move_speed = 250
		self.shot_manager = ShotManager()
	
	# Override
	def update(self, delta):
		keys_down = pygame.key.get_pressed()
		
		if keys_down[pygame.K_LEFT]:
			self.rect.x -= self.move_speed * delta
		if keys_down[pygame.K_RIGHT]:
			self.rect.x += self.move_speed * delta
			
		# Detect screen bounds
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x + self.rect.width >= SCREEN_WIDTH:
			self.rect.x = SCREEN_WIDTH - self.rect.width
			
		# Draw
		self.shot_manager.update(delta)
	
	def draw(self, screen):
		self.shot_manager.draw(screen)
		screen.blit(self.image, self.rect)


class Alien(pygame.sprite.Sprite):
	"""
	Primary enemy.
	"""
	# Constructor
	def __init__(self, x = 0, y = 0):
		super().__init__()
		self.image = pygame.transform.scale(assets.IMAGES['alien'], (48, 48))
		self.rect = self.image.get_rect()
		self.wait_time = 0
		
	def set_position(self, x, y):
		self.rect.x, self.rect.y = x, y


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
	def update(self, *args):
		delta = args[0]
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