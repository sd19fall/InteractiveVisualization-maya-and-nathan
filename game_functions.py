import sys
import pygame

from bolts import Bolt
from enemies import Enemy

def check_keydown_events(event, sf_settings, screen, ship, bolts, enemies):
	"""Respond to keypresses"""
	if event.key == pygame.K_RIGHT:
		ship.turn_right = True
	elif event.key == pygame.K_LEFT:
		ship.turn_left = True		
	elif event.key == pygame.K_UP:
		ship.forward_thrust = True
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

def check_keyup_events(event, ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.turn_right = False
	elif event.key == pygame.K_LEFT:
		ship.turn_left = False	
	elif event.key == pygame.K_UP:
		ship.forward_thrust = False
		
		
def check_events(sf_settings, screen, ship, bolts, enemies):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, sf_settings, screen, ship, bolts, enemies)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			

#def menu(sf_settings, screen)
			
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
		
def check_game_over(stats): 
	if stats.game_over == True:
		print('\n\n\tFinal Score -  ' + str(stats.score) + '\n')
		
		with open('high_score.txt') as file_object:
			previous = file_object.read()
		
		if stats.score > int(previous):
			print('\tCongrats,\n\tNew High Score!')
			with open('high_score.txt', 'w') as file_object:
				file_object.write(str(stats.score))
		
		print('\n\n\tGAME OVER')
		sys.exit()
			

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText


def menu_loop(settings, screen):

	#screen.fill(blue)
	selected="start"

	title=text_format("StarFighter", settings.font, 90, settings.yellow)
	if selected=="start":
		text_start=text_format("Start", settings.font, 75, settings.white)
	else:
		text_start = text_format("Start", settings.font, 75, settings.black)
	if selected=="quit":
		text_quit=text_format("Quit", settings.font, 75, settings.white)
	else:
		text_quit = text_format("Quit", settings.font, 75, settings.black)

	title_rect=title.get_rect()
	start_rect=text_start.get_rect()
	quit_rect=text_quit.get_rect()

	# Main Menu Text
	screen.blit(title, (settings.screen_width/2 - (title_rect[2]/2), 80))
	screen.blit(text_start, (settings.screen_width/2 - (start_rect[2]/2), 300))
	screen.blit(text_quit, (settings.screen_width/2 - (quit_rect[2]/2), 360))
	pygame.display.update()
	pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")