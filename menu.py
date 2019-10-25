import pygame
import sys
import os
from sf_settings import Settings
import game_functions as gf


# pygame.init()
 
# # Center the Game Application
# os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# # Game Resolution
# screen_width=800
# screen_height=600
# screen=pygame.display.set_mode((screen_width, screen_height))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
 
# # Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = "Airstream.ttf"
 
# # Game Framerate
# clock = pygame.time.Clock()
# FPS=30

def main_menu(screen, sf_settings):
 
    menu=True
    selected="start"
 
    while menu:
         
        # Main Menu UI
        screen.fill(blue)
        title=text_format("StarFighter", font, 90, yellow)
        if selected=="start":
            text_start=text_format("Start", font, 75, white)
        else:
            text_start = text_format("Start", font, 75, black)
        if selected=="quit":
            text_quit=text_format("Quit", font, 75, white)
        else:
            text_quit = text_format("Quit", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (sf_settings.screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (sf_settings.screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (sf_settings.screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")


