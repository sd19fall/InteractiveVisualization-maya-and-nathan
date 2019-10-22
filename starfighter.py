# REVAMP

import pygame
from pygame.sprite import Group

from sf_settings import Settings
from ship import Ship
from enemies import Enemy
import game_functions as gf
from game_stats import GameStats
import menu


def run_game():
	# Initialize pygame, settings, and screen object
	pygame.init()
	sf_settings = Settings()
	stats = GameStats(sf_settings)
	#stats.reset_stats()
	
	screen = pygame.display.set_mode(
		(sf_settings.screen_width, sf_settings.screen_height))
	pygame.display.set_caption("STARFIGHTER")
	pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

	# Make a ship
	ship = Ship(sf_settings, screen)
	
	# Make a group for bolts
	bolts = Group()
	
	# Make a group for enemies 
	enemies = Group()
	
	# Start the main loop for the game
	while True:
		gf.check_events(sf_settings, screen, ship, bolts, enemies)
		ship.update(sf_settings)
		gf.update_bolts(enemies, bolts, stats)
		gf.update_enemies(sf_settings, ship, screen, enemies, stats)
		gf.update_screen(sf_settings, screen, ship, enemies, bolts)
		pygame.display.set_caption("STARFIGHTER Extra Lives Left: " + 
			str(ship.ships_left - 1)  + '   Score: ' + str(stats.score))
		gf.check_game_over(stats)

		#menu.main_menu(screen)


run_game()

