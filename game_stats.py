class GameStats():
	"""Track statistics for STARFIGHTER"""
	
	def __init__(self, sf_settings):
		"""Initialize statistics"""
		self.sf_settings = sf_settings
		#self.reset_stats()
		
		#def reset_stats(self):
		"""Initialize statistics that can change during game"""
		self.ships_left = self.sf_settings.ship_count
		self.score = 0
		self.enemy_time = 0
		self.game_over = False

