'''
Created on 25 jun 2013

@author: Linus
'''

import glob
import Tile
import Boulder
import Player
import pygame

class Map:
    def __init__(self):
        self.advanceSound = pygame.mixer.Sound('sounds/advance.wav')
        
        self.endSprite = pygame.image.load('sprites/end.png')
        self.floorSprite = pygame.image.load('sprites/floor.png')
        self.wallSprite = pygame.image.load('sprites/wall.png')
        self.iceSprite = pygame.image.load('sprites/ice.png')
        
        self.currentMap = 0
        self.player = Player.Player((0, 0)) # Init player (to fix mainloop bug)
        self.end = Tile.Tile((0, 0), self.endSprite)
        self.screen = pygame.display.get_surface()
        self.maps = []
        self.objects = []
        self.boulders = [] # Used to draw boulders last
        for e in glob.glob('maps/*.map'):
            self.maps.append(e)
            
    def advanceMap(self):
        self.advanceSound.play()
        self.currentMap += 1
        
    def initMap(self):
        self.objects.clear()
        self.boulders.clear()
        try:
            if not (self.loadMap()):
                return False
        except:
            return False
        
        return True
    
    def draw(self):
        
        for t in self.objects:
            self.screen.blit(t.getImage(), t.getPos())
        
        for b in self.boulders:
            self.screen.blit(b.getImage(), b.getPos())
            
        self.screen.blit(self.end.getImage(), self.end.getPos())
        self.screen.blit(self.player.getImage(), self.player.getPos())
        
        
    def loadMap(self):
        mapName = self.maps[self.currentMap]
        try:
            file = open(mapName, 'r')
        except:
            return False
        
        mapContent = []
        for line in file:
            line = line.rstrip('\n')
            for e in range(0, len(line)):
                mapContent.append(line[e])
                
        counter = 0
        for e in range(0,30):
            for d in range(0,30):
                t = mapContent[counter]
                
                if (t == '#'):
                    self.objects.append(Tile.Tile((d*32, e*32), self.wallSprite, walkable=False))
                elif (t == 'I' or t =='$' or t == '%' or t =='&'):
                    self.objects.append(Tile.Tile((d*32, e*32), self.iceSprite, glidable=True))
                # If the tile is a player, boulder or the end, add a background tile
                else:
                    self.objects.append(Tile.Tile((d*32, e*32), self.floorSprite))
                    
                if (t == 'E' or t == '&'):
                    self.end = Tile.Tile((d*32, e*32), self.endSprite)
                elif (t == 'S' or t =='$'):
                    self.boulders.append(Boulder.Boulder((d*32, e*32)))
                elif (t == 'P' or t =='%'):
                    self.player = Player.Player((d*32, e*32))
                    
                counter += 1
        return True
    
    def getCurrentMap(self):
        return self.currentMap
    
    def getBoulders(self):
        return self.boulders
            
    def getTiles(self):
        return self.objects
    
    def getPlayer(self):
        return self.player
    
    def getEnd(self):
        return self.end