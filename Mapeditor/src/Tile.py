'''
Created on 28 jun 2013

@author: Linus
'''

import pygame

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, pos, currentImage=0, ice=False):
        pygame.sprite.Sprite.__init__(self)
        
        # Load tile images
        self.tileTypes = [pygame.image.load('sprites/wall.png'),
                          pygame.image.load('sprites/floor.png'),
                          pygame.image.load('sprites/rock.gif'),
                          pygame.image.load('sprites/playerdown1.gif'),
                          pygame.image.load('sprites/end.png'),
                          pygame.image.load('sprites/ice.png')]
        
        # Set default image
        self.currentImage = currentImage
        
        # Set ice mode
        self.ice = ice
        
        if (self.currentImage == 1 and self.ice):
            self.image = self.tileTypes[5]
        else:
            self.image = self.tileTypes[self.currentImage]
            
        self.pos = pos
        self.rect = pygame.Rect(self.pos, (32, 32))
        
    def getImage(self):
        return self.image
    
    def getType(self):
        if (self.getImage() == self.tileTypes[0]):
            return '#'
        elif (self.getImage() == self.tileTypes[1]):
            return '.'
        elif (self.getImage() == self.tileTypes[2] and self.ice):
            return '$'
        elif (self.getImage() == self.tileTypes[2] and not self.ice):
            return 'S'
        elif (self.getImage() == self.tileTypes[3] and not self.ice):
            return 'P'
        elif (self.getImage() == self.tileTypes[3] and self.ice):
            return '%'
        elif (self.getImage() == self.tileTypes[4] and not self.ice):
            return 'E'
        elif (self.getImage() == self.tileTypes[4] and self.ice):
            return '&'
        elif (self.getImage() == self.tileTypes[5]):
            return 'I'
    
    def setImage(self, reverse, ice):
        self.ice = ice
        if (reverse):
            if (self.currentImage == 0):
                self.currentImage = len(self.tileTypes)-2
            else:
                self.currentImage -= 1
        else:
            if (self.currentImage == len(self.tileTypes)-2):
                self.currentImage = 0
            else:
                self.currentImage += 1
                
        if (self.currentImage == 1 and self.ice):
            self.image = self.tileTypes[5]
        else:
            self.image = self.tileTypes[self.currentImage]
    
    def getPos(self):
        return self.pos
    
    def checkCollision(self, pos):
        if (self.rect.collidepoint(pos)):
            return True
        else:
            return False