"""
Software Design f2019
Mini Project 4
STARFIGHTER arcade game

This is a 2D spaceship shooting game based off the 
classic arcade game ASTEROIDS. To play, enter 
[python starfighter.py] in terminal!

@author: Nathan, Maya 

"""

import pygame
from pygame.sprite import Group

from sf_settings import Settings
from ship import Ship
from enemies import Enemy
import game_functions as gf
from game_stats import GameStats
from menu import Menu


def run_game():
	# Initialize pygame, settings, stats, and screen object
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
	
	# Make mouse invisible
	pygame.mouse.set_visible(False)

	# Initializes music 
	pygame.mixer.init()
	pygame.mixer.music.load('music/StarWars.mp3')
	pygame.mixer.music.play()

	# Start the main loop for the game
	while True:
		"""
		Main game loop, runs constantly updating the screen and all variables
		"""

		# Checks for keyboard events
		gf.check_events(sf_settings, screen, ship, bolts, enemies, menu, stats)

		# Updates ship, bolt, and enemy spites
		ship.update(sf_settings)
		gf.update_bolts(enemies, bolts, stats)
		gf.update_enemies(sf_settings, ship, screen, enemies, stats)

		# Updates screen
		gf.update_screen(sf_settings, screen, ship, enemies, bolts, menu, stats)
		pygame.display.set_caption("STARFIGHTER Extra Lives Left: " + 
			str(ship.ships_left - 1)  + '   Score: ' + str(stats.score))

		# Checks for game over
		gf.check_game_over(sf_settings, screen, menu, ship, enemies, bolts, stats)

		# Menu screen loop
		while sf_settings.menu == True:
			gf.check_events(sf_settings, screen, ship, bolts, enemies, menu, stats)
			gf.menu_loop(sf_settings, screen, menu, ship, enemies, bolts, stats)

		# Game over screen loop
		while stats.game_over == True:
			gf.check_events(sf_settings, screen, ship, bolts, enemies, menu, stats)
			gf.game_over(sf_settings, screen, menu, ship, enemies, bolts, stats)

		# Updates game difficulty
		gf.difficulty(stats, sf_settings)



run_game()

