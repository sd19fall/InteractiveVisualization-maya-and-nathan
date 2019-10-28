# REVAMP

import pygame
from pygame.sprite import Group

from sf_settings import Settings
from ship import Ship
from enemies import Enemy
import game_functions as gf
from game_stats import GameStats
from menu import Menu


def run_game():
	# Initialize pygame, settings, and screen object
	pygame.init()
	sf_settings = Settings()
	stats = GameStats(sf_settings)
	menu = Menu(sf_settings)
	
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
	
	pygame.mouse.set_visible(False)
	# Start the main loop for the game
	while True:
		gf.check_events(sf_settings, screen, ship, bolts, enemies, menu, stats)

		#stats.reset(sf_settings)
		ship.update(sf_settings)
		gf.update_bolts(enemies, bolts, stats)
		gf.update_enemies(sf_settings, ship, screen, enemies, stats)
		gf.hud(sf_settings, screen, menu, ship, enemies, bolts, stats)

		gf.update_screen(sf_settings, screen, ship, enemies, bolts)
		pygame.display.set_caption("STARFIGHTER Extra Lives Left: " + 
			str(ship.ships_left - 1)  + '   Score: ' + str(stats.score))
		gf.check_game_over(sf_settings, screen, menu, ship, enemies, bolts, stats)

		while sf_settings.menu == True:
			gf.check_events(sf_settings, screen, ship, bolts, enemies, menu, stats)
			gf.menu_loop(sf_settings, screen, menu, ship, enemies, bolts, stats)

		while stats.game_over == True:
			gf.check_events(sf_settings, screen, ship, bolts, enemies, menu, stats)
			gf.game_over(sf_settings, screen, menu, ship, enemies, bolts, stats)


run_game()

