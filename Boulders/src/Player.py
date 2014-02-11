'''
Created on 27 jun 2013

@author: Linus
'''

import MovableObject
import pygame

class Player(MovableObject.MovableObject):
    '''
    @summary: A player in the game
    '''
    
    def __init__(self, pos):
        '''
        @param pos:  The position for the player
        '''
        MovableObject.MovableObject.__init__(self, pos, pygame.image.load('sprites/(0, 32)1.gif'))
        
    def changeDirection(self):
        '''
        @summary: Changes the direction image for the player
        '''
        self.image = pygame.image.load('sprites/'+str(self.direction)+'1.gif')
        
    def move(self):
        self.pos = (self.pos[0] + self.xVel, self.pos[1] + self.yVel)
        self.counter += 1
        if (self.counter == 5):
            self.image = pygame.image.load('sprites/'+str(self.direction)+'2.gif')
        elif (self.counter == 11):
            self.image = pygame.image.load('sprites/'+str(self.direction)+'3.gif')
        elif (self.counter == 15):
            self.changeDirection()
        if (self.counter == 16):
            if (self.isGliding):
                self.counter = 0
                self.isMoving = False
            else:
                self.resetDirection()