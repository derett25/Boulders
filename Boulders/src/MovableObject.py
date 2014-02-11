'''
Created on 10 aug 2013

@author: Linus
'''

import GameObject

class MovableObject(GameObject.GameObject):
    
    def __init__(self, pos, image):
        GameObject.GameObject.__init__(self, pos, image)
        self.isMoving = False
        self.isGliding = False
        self.xVel = 0
        self.yVel = 0
        self.counter = 0
        self.direction = (0, 0)
        
    def setGlide(self):
        self.isGliding = True
        self.isMoving = True
    
    def setDirection(self, direction):
        self.direction = direction
        self.xVel = self.direction[0]/16
        self.yVel = self.direction[1]/16
        self.isMoving = True
    
    def resetDirection(self):
        self.counter = 0
        self.direction = (0, 0)
        self.xVel = 0
        self.yVel = 0
        self.isMoving = False
        self.isGliding = False
        
    def getMoving(self):
        return self.isMoving
    
    def getGliding(self):
        return self.isGliding
    
    def getDirection(self):
        return self.direction
