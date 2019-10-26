import pygame

class Settings():
	"""A class to store all the settings for Alien Invasion"""
	
	
	def __init__(self):
		"""Initialize the game's settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_image = pygame.image.load('images/stars.png')

		self.font = "Airstream.ttf"
		self.menu = True

		self.theme = 'Star Wars'

		# Ship settings
		self.ship_image = pygame.image.load('images/StarWars/ship.png')
		self.ship_engine_image = pygame.image.load('images/StarWars/ship_engines.png')
		self.ship_thrust_factor = 1
		self.starting_fuel = 1000
		self.ship_count = 3
		self.turn_rate = 10

		# Phaser settings
		self.bolt_image = pygame.image.load('images/StarWars/bolts.png')
		self.bolt_speed_factor = 50
		self.bolt_width = 2
		self.bolt_length = 20
		self.bolts_allowed = 100
		self.bolt_life = 10
		
		# Enemy settings
		self.enemy_image = pygame.image.load('images/StarWars/tie_fighter.png')
		self.enemy_count = 10
		self.enemy_speed = 5
		self.enemy_time = 10

		# Level one settings
		self.lvl_1_coefficent = 10
		self.lvl_2_coefficent = 15
		self.lvl_3_coefficent = 20

		# Color settings
		self.white=(255, 255, 255)
		self.black=(0, 0, 0)
		self.gray=(170, 170, 170)
		self.red=(255, 0, 0)
		self.green=(0, 255, 0)
		self.blue=(0, 0, 255)
		self.yellow=(255, 255, 0)

# class SettingsST():
# 	"""A class to store all the settings for Alien Invasion"""
	
	
# 	def __init__(self):
# 		"""Initialize the game's settings"""
# 		# Screen settings
# 		self.screen_width = 1200
# 		self.screen_height = 800
# 		self.bg_image = pygame.image.load('images/stars.png')

# 		self.font = "Airstream.ttf"
# 		self.menu = False

# 		# Ship settings
# 		self.ship_image = pygame.image.load('images/StarTrek/USSENTERPRISE.png')
# 		#self.ship_engine_image = pygame.image.load('images/ship_engines.png') #add engine fire to enterprise
# 		self.ship_thrust_factor = 1
# 		self.starting_fuel = 1000
# 		self.ship_count = 3
# 		self.turn_rate = 10

# 		# Phaser settings
# 		self.bolt_image = pygame.image.load('images/StarTrek/comp and comm.png')
# 		self.bolt_speed_factor = 50
# 		self.bolt_width = 2
# 		self.bolt_length = 20
# 		self.bolts_allowed = 100
# 		self.bolt_life = 10
		
# 		# Enemy settings
#		self.enemy_image = pygame.image.load('images/StarTrek/jupiter.png')
# 		self.enemy_count = 10
# 		self.enemy_speed = 5
# 		self.enemy_time = 10

# 		# Level one settings
# 		self.lvl_1_coefficent = 10
# 		self.lvl_2_coefficent = 15
# 		self.lvl_3_coefficent = 20

# 		# Color settings
# 		self.white=(255, 255, 255)
# 		self.black=(0, 0, 0)
# 		self.gray=(50, 50, 50)
# 		self.red=(255, 0, 0)
# 		self.green=(0, 255, 0)
# 		self.blue=(0, 0, 255)
# 		self.yellow=(255, 255, 0)

# class SettingsHP():
# 	"""A class to store all the settings for Alien Invasion"""
	
	
# 	def __init__(self):
# 		"""Initialize the game's settings"""
# 		# Screen settings
# 		self.screen_width = 1200
# 		self.screen_height = 800
# 		self.bg_image = pygame.image.load('images/Harry/hogwarts.png')

# 		self.font = "Airstream.ttf"
# 		self.menu = False

# 		# Ship settings
# 		self.ship_image = pygame.image.load('images/Harry/harry.png')
# 		self.ship_thrust_factor = 1
# 		self.starting_fuel = 1000
# 		self.ship_count = 3
# 		self.turn_rate = 10

# 		# Phaser settings
# 		self.bolt_image = pygame.image.load('images/StarTrek/comp and comm.png') #create patronus 
# 		self.bolt_speed_factor = 50
# 		self.bolt_width = 2
# 		self.bolt_length = 20
# 		self.bolts_allowed = 100
# 		self.bolt_life = 10
		
# 		# Enemy settings
#		self.enemy_image = pygame.image.load('images/Harry/dementor.png') 
# 		self.enemy_count = 10
# 		self.enemy_speed = 5
# 		self.enemy_time = 10

# 		# Level one settings
# 		self.lvl_1_coefficent = 10
# 		self.lvl_2_coefficent = 15
# 		self.lvl_3_coefficent = 20

# 		# Color settings
# 		self.white=(255, 255, 255)
# 		self.black=(0, 0, 0)
# 		self.gray=(50, 50, 50)
# 		self.red=(255, 0, 0)
# 		self.green=(0, 255, 0)
# 		self.blue=(0, 0, 255)
# 		self.yellow=(255, 255, 0)

# class SettingsD():
# 	"""A class to store all the settings for Alien Invasion"""
	
	
# 	def __init__(self):
# 		"""Initialize the game's settings"""
# 		# Screen settings
# 		self.screen_width = 1200
# 		self.screen_height = 800
# 		self.bg_image = pygame.image.load('images/Disney/disney.png')

# 		self.font = "Airstream.ttf"
# 		self.menu = False

# 		# Ship settings
# 		self.ship_image = pygame.image.load('images/Disney/mickey mouse.png')
# 		self.ship_thrust_factor = 1
# 		self.starting_fuel = 1000
# 		self.ship_count = 3
# 		self.turn_rate = 10

# 		# Phaser settings
# 		#self.bolt_image = pygame.image.load('images/Disney/mickey mouse.png') #create hearts
# 		self.bolt_speed_factor = 50
# 		self.bolt_width = 2
# 		self.bolt_length = 20
# 		self.bolts_allowed = 100
# 		self.bolt_life = 10
		
# 		# Enemy settings
#		self.enemy_image = pygame.image.load('images/Disney/minnie mouse.png') 
# 		self.enemy_count = 10
# 		self.enemy_speed = 5
# 		self.enemy_time = 10

# 		# Level one settings
# 		self.lvl_1_coefficent = 10
# 		self.lvl_2_coefficent = 15
# 		self.lvl_3_coefficent = 20

# 		# Color settings
# 		self.white=(255, 255, 255)
# 		self.black=(0, 0, 0)
# 		self.gray=(50, 50, 50)
# 		self.red=(255, 0, 0)
# 		self.green=(0, 255, 0)
# 		self.blue=(0, 0, 255)
# 		self.yellow=(255, 255, 0)