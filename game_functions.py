import sys
import pygame

from bolts import Bolt
from enemies import Enemy

def check_keydown_events(event, sf_settings, screen, ship, bolts, enemies, menu, stats):
	"""Respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		ship.turn_right = True
		if sf_settings.menu == True:
			if menu.selected == 1:
				if menu.current_theme < len(menu.themes)-1:
					menu.current_theme += 1

	elif event.key == pygame.K_LEFT:
		ship.turn_left = True		
		if sf_settings.menu == True:
			if menu.selected == 1:
				if menu.current_theme > 0:
					menu.current_theme -= 1

	elif event.key == pygame.K_UP:
		ship.forward_thrust = True
		if sf_settings.menu == True:
			if menu.selected > 0:
				menu.selected -= 1

	elif event.key == pygame.K_DOWN:
		if sf_settings.menu == True:
			if menu.selected < 2:
				menu.selected += 1

	elif event.key == pygame.K_SPACE:
		fire_bolt(sf_settings, screen, ship, bolts)

	elif event.key == pygame.K_e:
		new_enemy(sf_settings, screen, enemies)

	elif event.key == pygame.K_q:
		sys.exit()

	elif event.key == pygame.K_ESCAPE:
		if sf_settings.menu == False:
			sf_settings.menu = True
		else:
			sf_settings.menu = False

	if event.key == pygame.K_RETURN:
		if menu.selected == 0:
			sf_settings.menu = False
		elif menu.selected == 1:
			if menu.current_theme == 0:
				starwars(sf_settings)
			if menu.current_theme == 1:
				startrek(sf_settings)
			if menu.current_theme == 2:
				harrypotter(sf_settings)
		elif menu.selected == 2:
			sys.exit()
		
		if stats.game_over == True:
			stats.game_over = False
		
def check_keyup_events(event, ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.turn_right = False
	elif event.key == pygame.K_LEFT:
		ship.turn_left = False	
	elif event.key == pygame.K_UP:
		ship.forward_thrust = False
		
def check_events(sf_settings, screen, ship, bolts, enemies, menu, stats):
	"""Respond to keypresses events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, sf_settings, screen, ship, bolts, enemies, menu, stats)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
						
def fire_bolt(sf_settings, screen, ship, bolts):
	# Create a new bolt and add it to bolts group
	new_bolt = Bolt(sf_settings, screen, ship)
	bolts.add(new_bolt)
		
def new_enemy(sf_settings, screen, enemies):
	# Create a new enemy and add it to enemies group
	if len(enemies) < sf_settings.enemy_count:
		new_enemy = Enemy(sf_settings, screen)
		enemies.add(new_enemy)

def update_screen(sf_settings, screen, ship, enemies, bolts):
	"""Update images on screen and flip to new screen"""
		
	# Redraw the screen during each pass through the loop
	screen.blit(sf_settings.bg_image, [0, 0])
	for bolt in bolts.sprites():
		bolt.draw_bolt()
	for enemy in enemies.sprites():
		enemy.blitme()
	ship.blitme()
		
	# Make the most recenly drawn screen visible
	pygame.display.flip()

def update_bolts(enemies, bolts, stats):
	"""Update position of bolts, and get rid of old ones"""
	bolts.update()
	
	# Get rid of bolts after a certian age
	for bolt in bolts.copy():
		if bolt.age <= 0:
			bolts.remove(bolt)
			
	# If any bolts have hit enemies, remove bolts and enemy
	collisions = pygame.sprite.groupcollide(bolts, enemies, True, True)
	
	if collisions:
		stats.score += 1

def update_enemies(sf_settings, ship, screen, enemies, stats):
	enemies.update()

	if stats.enemy_time == 20:
		new_enemy(sf_settings, screen, enemies)
		stats.enemy_time = 0
		
	stats.enemy_time += 1

	# look for enemy-player collisions
	
	hit_list = pygame.sprite.spritecollide(ship, enemies, True)
	for enemy in hit_list:
		ship.ship_hit(sf_settings, stats)
		
def check_game_over(sf_settings, screen, menu, ship, enemies, bolts, stats): 
	if stats.game_over == True:
		print('\n\n\tFinal Score -  ' + str(stats.score) + '\n')
		
		with open('high_score.txt') as file_object:
			previous = file_object.read()
		
		if stats.score > int(previous):
			print('\tCongrats,\n\tNew High Score!')
			with open('high_score.txt', 'w') as file_object:
				file_object.write(str(stats.score))
		
		print('\n\n\tGAME OVER')

		game_over(sf_settings, screen, menu, ship, enemies, bolts, stats)
			
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def menu_loop(settings, screen, menu, ship, enemies, bolts, stats):

	#screen.fill(settings.blue)

	title = text_format("StarFighter", settings.font, 90, settings.yellow)

	if menu.selected == 0:
		text_start = text_format("Start", settings.font, 65, settings.white)
	else:
		text_start = text_format("Start", settings.font, 65, settings.gray)
	if menu.selected == 1:
		text_theme = text_format(str('< ' + menu.themes[menu.current_theme] + ' >'), settings.font, 65, settings.white)
	else:
		text_theme = text_format(str('< ' + menu.themes[menu.current_theme] + ' >'), settings.font, 65, settings.gray)
	if menu.selected == 2:
		text_quit = text_format("Quit", settings.font, 65, settings.white)
	else:
		text_quit = text_format("Quit", settings.font, 65, settings.gray)


	title_rect = title.get_rect()
	start_rect = text_start.get_rect()
	theme_rect = text_theme.get_rect()
	quit_rect = text_quit.get_rect()

	update_screen(settings, screen, ship, enemies, bolts)

	screen.blit(title, (settings.screen_width/2 - (title_rect[2]/2), 80))
	screen.blit(text_start, (settings.screen_width/2 - (start_rect[2]/2), 300))
	screen.blit(text_theme, (settings.screen_width/2 - (theme_rect[2]/2), 370))
	screen.blit(text_quit, (settings.screen_width/2 - (quit_rect[2]/2), 440))
	pygame.display.update()
	pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

def game_over(settings, screen, menu, ship, enemies, bolts, stats):

	#screen.fill(settings.blue)

	game_over = text_format("Game Over", settings.font, 90, settings.yellow)
	return_to_menu = text_format("Return", settings.font, 60, settings.white)
	score = text_format("Score: " + str(stats.score), settings.font, 60, settings.white)

	# Finds centers of text to center in window 
	go_rect = game_over.get_rect()
	return_rect = return_to_menu.get_rect()
	score_rect = score.get_rect()


	update_screen(settings, screen, ship, enemies, bolts)

	screen.blit(game_over, (settings.screen_width/2 - (go_rect[2]/2), 100))
	screen.blit(score, (settings.screen_width/2 - (score_rect[2]/2), 320))
	screen.blit(return_to_menu, (settings.screen_width/2 - (return_rect[2]/2), 420))

	pygame.display.update()
	pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

def starwars(settings):
	settings.bg_image = pygame.image.load('images/stars.png')
	settings.ship_image = pygame.image.load('images/StarWars/ship.png')
	settings.ship_engine_image = pygame.image.load('images/StarWars/ship_engines.png')
	settings.bolt_image = pygame.image.load('images/StarWars/bolts.png')
	settings.enemy_image = pygame.image.load('images/StarWars/tie_fighter.png')

def startrek(settings):
	settings.bg_image = pygame.image.load('images/stars.png')
	settings.ship_image = pygame.image.load('images/StarTrek/USSENTERPRISE.png')
	settings.bolt_image = pygame.image.load('images/StarTrek/comp and comm.png')
	settings.enemy_image = pygame.image.load('images/StarTrek/jupiter.png')

def harrypotter(settings):

	settings.bg_image = pygame.image.load('images/Harry/hogwarts.png')
	settings.ship_image = pygame.image.load('images/Harry/harry.png')
	settings.enemy_image = pygame.image.load('images/Harry/dementor.png') 

#def disney(settings):
#	settings.bg_image = pygame.image.load('image/Disney/disney.png)
#	settings.ship_image = pygame.image.load('images/Disney/mickey mouse.png')
#	settings.enemy_image = pygame.image.load('images/Disney/minnie mouse.png') 

	