import pygame
from pygame.sprite import Sprite
from math import sin, cos, radians, fabs

class Bolt(Sprite):
	"""A class to manage laser bolts fired from ship"""
	
	def __init__(self, sf_settings, screen, ship):
		"""Create a bullet object at the ship's position"""
		super(Bolt, self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# Create a bolt rect at (0, 0) and then set correct position and angle
		self.image = pygame.transform.rotate(sf_settings.bolt_image, ship.angle)
		self.rect = self.image.get_rect()

		# Sets starting position at ship's position
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# Sets speed and direction				
		self.speed_y = ship.speed_y + cos(radians(ship.angle)) * sf_settings.bolt_speed_factor
		self.speed_x = -ship.speed_x + sin(radians(ship.angle)) * sf_settings.bolt_speed_factor
		
		# Sets bullet age
		self.age = sf_settings.bolt_life

	
	def update(self):
		"""Move the bolt up screen"""
		# Update position
		self.rect.y -= self.speed_y
		self.rect.x -= self.speed_x
		self.age -= 1
		
		# If hit edge of screen, go to other side
		if self.rect.centery <= 0:
			self.rect.centery = self.screen_rect.bottom - 2
		if self.rect.centery >= self.screen_rect.bottom:
			self.rect.centery = self.screen_rect.top + 2		
		
		if self.rect.centerx <= 0:
			self.rect.centerx = self.screen_rect.right - 2
		if self.rect.centerx >= self.screen_rect.right:
			self.rect.centerx = 2

		
	def draw_bolt(self):
		"""Draw the bullet to the screen"""
		self.screen.blit(self.image, self.rect)

	
	def blow_up(self, enemies):
		print('boom')
