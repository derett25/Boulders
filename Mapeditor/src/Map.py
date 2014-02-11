'''
Created on 28 jun 2013

@author: Linus
'''

import pygame
import Tile
import glob

class Map:
    
    def __init__(self):
        self.tiles = []
        self.backgroundFloor = pygame.image.load('sprites/floor.png')
        self.iceFloor = pygame.image.load('sprites/ice.png')
        self.screen = pygame.display.get_surface()
        self.iceMode = False
        
    def initMap(self):
        self.tiles.clear()
        for e in range(0,30):
                for d in range(0,30):
                    self.tiles.append(Tile.Tile((d*32, e*32)))
                    
    def switchTile(self, pos, reverse):
        for e in self.tiles:
            if (e.checkCollision(pos)):
                e.setImage(reverse, self.iceMode)
    
    def getMap(self):
        return self.tiles
    
    def switchMode(self):
        self.iceMode = not self.iceMode
    
    def draw(self):
        for t in self.getMap():
            
            # Draw a background tile depending on what type the tile is
            if (t.getType() == 'P' or t.getType() == 'S' or t.getType() == 'E'):
                self.screen.blit(self.backgroundFloor, t.getPos())
            elif (t.getType() == '%' or t.getType() == '$' or t.getType() == '&'):
                self.screen.blit(self.iceFloor, t.getPos())
                
            self.screen.blit(t.getImage(), t.getPos())
            if (t.checkCollision(pygame.mouse.get_pos())):
                # Create a transparent rectangle
                rect = pygame.Surface((32,32))
                rect.set_alpha(90) # Set alpha to create transparency
                rect.fill((14,198,31))
                self.screen.blit(rect, t.getPos())
            
    def exportMap(self):
        try:
            fileContent = []
            foundEnd = False
            foundPlayer = 0
            count = 0
            for e in range(0,30):
                for d in range(0,30):
                    if (self.tiles[count].getType() == 'P' or self.tiles[count].getType() == '%'):
                        foundPlayer += 1
                    elif (self.tiles[count].getType() == 'E' or self.tiles[count].getType() == '&'):
                        foundEnd = True
                    fileContent.append(self.tiles[count].getType())
                    count += 1
                fileContent.append('\n')
                    
            if (not foundEnd or foundPlayer == 0 or foundPlayer > 1):
                return False
            
            file = open('maps/map.map','w')
            for e in fileContent:
                file.write(e)
            file.close()
        except:
            return False
        
        return True
        
    def importMap(self):
        files = []
        for e in glob.glob('maps/*.map'):
            files.append(e)
        mapString = []
        try:
            file = open(files[0], 'r')
        except:
            return False
        
        for line in file:
            line = line.rstrip('\n')
            for e in range(0, len(line)):
                mapString.append(line[e])
                
        self.tiles.clear()
        counter = 0
        for e in range(0,30):
            for d in range(0,30):
                if (mapString[counter] == '#'):
                    self.tiles.append(Tile.Tile((d*32, e*32)))
                elif (mapString[counter] == '.'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 1))
                elif (mapString[counter] == 'S'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 2))
                elif (mapString[counter] == '$'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 2, ice=True))
                elif (mapString[counter] == 'P'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 3))
                elif (mapString[counter] == '%'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 3, ice = True))
                elif (mapString[counter] == 'E'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 4))
                elif (mapString[counter] == '&'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 4, ice = True))
                elif (mapString[counter] == 'I'):
                    self.tiles.append(Tile.Tile((d*32, e*32), 1, ice=True))
                counter += 1
        return True
        