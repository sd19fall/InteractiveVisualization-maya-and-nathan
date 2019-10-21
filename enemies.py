import pygame
from pygame.sprite import Sprite
import random

class Enemy(Sprite):
	"""A class to represent enemy ships"""
	
	def __init__(self, sf_settings, screen):
		"""Initialize enemy and starting position"""
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.sf_settings = sf_settings
		
		# Load image and set rect attribute
		self.image = pygame.image.load('images/tie_fighter.png')
		self.rect = self.image.get_rect()
		
		# Starting position
		self.rect.x = random.randint(0, 1200)
		self.rect.y = self.rect.height
		
		self.speed_y = random.randint(-sf_settings.enemy_speed, sf_settings.enemy_speed)
		self.speed_x = random.randint(-sf_settings.enemy_speed, sf_settings.enemy_speed)
		
	def update(self):
		"""Update position"""
		self.rect.centery += self.speed_y
		self.rect.centerx += self.speed_x

		if self.rect.centery <= 0:
			self.rect.centery = self.screen_rect.bottom - 2
		if self.rect.centery >= self.screen_rect.bottom:
			self.rect.centery = self.screen_rect.top + 2		
		
		if self.rect.centerx <= 0:
			self.rect.centerx = self.screen_rect.right - 2
		if self.rect.centerx >= self.screen_rect.right:
			self.rect.centerx = 2
		
	
	def blitme(self):
		"""Draw the alien at current location"""
		self.screen.blit(self.image, self.rect)
