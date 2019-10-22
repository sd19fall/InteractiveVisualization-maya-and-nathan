import pygame
import sys
from math import sin, cos, radians

class Ship():
	
	def __init__(self, sf_settings, screen):
		"""Initialize the ship and set its starting position"""
		self.screen = screen
		self.sf_settings = sf_settings
				
		# Load the ship image and get its rect
		self.image = self.sf_settings.ship_image
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new ship at the bottom center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom - 50
		
		# Store a decimal value for the ship's center
		
		# Movement Flag
		self.turn_right = False
		self.turn_left = False
		self.forward_thrust = False
		
		# Initialize movement variables
		self.speed_y = 0
		self.speed_x = 0
		self.angle = 0
		
		# Initialize fuel variable based off set starting fuel
		self.fuel = sf_settings.starting_fuel
		
		# Initialize ships left variable
		self.ships_left = sf_settings.ship_count
		
		
	def update(self, sf_settings):
		"""Update the ships's position based on the movement flags"""
		
		# Recalculate angle based on movement flags
		if self.turn_right:
			self.angle -= sf_settings.turn_rate
		
		if self.turn_left:
			self.angle += sf_settings.turn_rate
				
				
		# Shuts off engines if no fuel is left
		if self.fuel > 0 and self.forward_thrust:		
			# Changes to engine on image and rotate
			self.image = pygame.transform.rotate(
				self.sf_settings.ship_engine_image, self.angle)
				
			# Increases component speed based on angle and thrust flag
			self.speed_y += cos(radians(self.angle)) * sf_settings.ship_thrust_factor
			self.speed_x += sin(radians(-self.angle)) * sf_settings.ship_thrust_factor
			
			# Decreases fuel
			self.fuel -= 1

	
		# Changes to engine off image and rotates to angle
		else:			
			self.image = pygame.transform.rotate(
				self.sf_settings.ship_image, self.angle)
			
		# Logic for recalculating position
		self.rect.centery -= self.speed_y
		self.rect.centerx += self.speed_x
		
		# If ship reaches edge of screen, move to opposite side
		if self.rect.centery <= 0:
			self.rect.centery = self.screen_rect.bottom - 2
		if self.rect.centery >= self.screen_rect.bottom:
			self.rect.centery = self.screen_rect.top + 2		
		
		if self.rect.centerx <= 0:
			self.rect.centerx = self.screen_rect.right - 2
		if self.rect.centerx >= self.screen_rect.right:
			self.rect.centerx = 2
		
	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
		
	def ship_hit(self, sf_settings, stats):
	
		self.ships_left -= 1
		if self.ships_left <= 0:
			stats.game_over = True
			
		else:
					
			# Resets variables 
			self.rect.centerx = self.screen_rect.centerx
			self.rect.bottom = self.screen_rect.bottom - 20
			
			self.angle = 0
			self.speed_y = 0
			self.speed_x = 0
			
			self.fuel = sf_settings.starting_fuel
