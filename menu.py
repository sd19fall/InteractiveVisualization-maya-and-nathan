import pygame
import sys
import os



class Menu():

    def __init__(self, sf_settings):

        self.selected = 0 


    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
    
        return newText