'''
Created on 28 jun 2013

@author: Linus
'''

import pygame

class GameObject():
    
    def __init__(self, pos, image):
        self.image = image
        self.pos = pos
    
    def setImage(self, image):
        self.image = image
        
    def setPos(self, pos):
        self.pos = pos
        
    def getPos(self):
        return self.pos
    
    def getImage(self):
        return self.image
    
    def getRect(self):
        return pygame.Rect(self.getPos(), (32, 32))
    
    def checkCollision(self, pos):
        return self.getRect().collidepoint(pos)