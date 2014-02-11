# -*- coding: utf-8 -*-

'''
Created on 18 jul 2013

@author: Linus
'''

import pygame

class Splash:
    
    def __init__(self):
        self.image = pygame.image.load('sprites/splash.png')
        self.running = True
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect((370, 480), (215, 45))
        
    def drawText(self, text, pos, color, size, bold):
        
        # Performance at main menu not important
        font = pygame.font.SysFont("Candara", size, bold)
        
        textRender = font.render(text, True, color)
        self.screen.blit(textRender, pos)
    
    def draw(self):
        self.screen.blit(self.image, (0, 0))
        if (self.rect.collidepoint(pygame.mouse.get_pos())):
            self.drawText("Start Game", (370, 480), (255, 0, 0), 45, 1)
        else:
            self.drawText("Start Game", (370, 480), (255, 255, 255), 45, 1)
        self.drawText('Copyright © Linus Esbjörnsson 2013', (730, 940), (255, 255, 255), 15, 0)
        self.drawText('Music by Daniel Kurtis', (10, 940), (255, 255, 255), 15, 0)
        
    def mainLoop(self):
        while(self.running):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): 
                    self.running = False
                    return False
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    if (self.rect.collidepoint(pygame.mouse.get_pos())):
                        self.running = False
            self.draw()
            pygame.display.flip()
            
        return True