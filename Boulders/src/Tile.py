'''
Created on 25 jun 2013

@author: Linus
'''

import GameObject

class Tile(GameObject.GameObject):
    def __init__(self, pos, image, walkable=True, glidable=False):
        GameObject.GameObject.__init__(self, pos, image)
        self.walkable = walkable
        self.glidable = glidable
    
    def getWalkable(self):
        return self.walkable
    
    def getGlidable(self):
        return self.glidable