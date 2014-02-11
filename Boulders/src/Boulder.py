'''
Created on 8 aug 2013

@author: Linus
'''

import MovableObject
import pygame

class Boulder(MovableObject.MovableObject):
    
    def __init__(self, pos):
        MovableObject.MovableObject.__init__(self, pos, pygame.image.load('sprites/boulder.gif'))
        self.boulderSound = pygame.mixer.Sound('sounds/boulder.wav')
    
    def move(self):
        self.pos = (self.pos[0] + self.xVel, self.pos[1] + self.yVel)
        self.counter += 1
        if (self.counter == 16):
            if (self.isGliding):
                self.counter = 0
                self.isMoving = False
            else:
                self.resetDirection()
                self.boulderSound.play()
        
