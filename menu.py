import pygame
import sys
import os



class Menu():

    def __init__(self, sf_settings):

        self.selected = 0 
        self.current_theme = 0
        self.themes = ['Star Wars', 'Star Trek', 'Harry Potter', 'Disney']
        self.block_width = 510
        self.rect = pygame.Rect(sf_settings.screen_width/2 - self.block_width/2, 65, self.block_width, 470)
        self.rect_shadow = pygame.Rect(sf_settings.screen_width/2 - self.block_width/2+10, 65+10, self.block_width, 470)


    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
    
        return newText