import pygame

class Settings():
	"""A class to store all the settings for Alien Invasion"""
	
	
	def __init__(self):
		"""Initialize the game's settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_image = pygame.image.load('images/stars.png')

		# Ship settings
		self.ship_image = pygame.image.load('images/ship.png')
		self.ship_engine_image = pygame.image.load('images/ship_engines.png')
		self.ship_thrust_factor = 1.5
		self.starting_fuel = 1000
		self.ship_count = 3

		# Phaser settings
		self.bolt_image = pygame.image.load('images/bolts.png')
		self.bolt_speed_factor = 50
		self.bolt_width = 2
		self.bolt_length = 20
		self.bolts_allowed = 100
		self.bolt_life = 10
		
		# Enemy settings
		self.enemy_count = 10
		self.enemy_speed = 12
		self.enemy_time = 20

		# Level one settings
		self.lvl_1_coefficent = 10
		self.lvl_2_coefficent = 15
		self.lvl_3_coefficent = 20

