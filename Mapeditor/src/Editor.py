'''
Created on 28 jun 2013

@author: Linus
'''

import pygame
import Map
import os
import time

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (400,50) # Code from http://www.pygame.org/wiki/SettingWindowPosition

class Editor:
    
    def __init__(self, width=960, height=960):
        pygame.init()
        
        self.colors = {'Red': (255, 0, 0), 'White': (255, 255, 255), 'Green': (0, 255, 0), 'Blue': (0, 0, 255), 'Black': (0, 0, 0), 'Yellow': (255, 255, 0)}
        self.textType = {'Normal': pygame.font.SysFont("Candara", 15), 'Big': pygame.font.SysFont("Candara", 25, bold=1)}
        
        
        pygame.display.set_caption('Boulders Map Editor')
        self.screen = pygame.display.set_mode((width, height))
        
        self.errorTimer = time.time()
        self.statusMessage = ''
        self.drawHelp = False
        self.running = True
        self.fpsLimit = pygame.time.Clock()
        self.setSplashScreen()
        self.map = Map.Map()
        self.map.initMap()
        
        # Initialize helptext
        self.helpText = self.drawText('How to?', (860, 0), self.colors['White'], "Big")
        
    def setSplashScreen(self):
        self.drawText('Loading...', (30, 900), self.colors['White'], "Big")
        pygame.display.flip()
        
    def drawText(self, text, pos, color, textType="Normal"):
        textRender = self.textType[textType].render(text, True, color)
        return self.screen.blit(textRender, (pos))
        
    def draw(self):
        self.map.draw()
        self.drawText(self.statusMessage, (10, 0), self.colors['Yellow'])
        
        if (self.drawHelp):
            self.helpText = self.drawText('How to?', (860, 0), self.colors['Red'], "Big")
            self.drawText('Left click to switch tile', (960/2-160, 150), self.colors['White'], "Big")
            self.drawText('Right click to switch tile anti-clockwise', (960/2-160, 200), self.colors['White'], "Big")
            self.drawText('ESC to clear the map', (960/2-160, 250), self.colors['White'], "Big")
            self.drawText('S to save the map', (960/2-160, 300), self.colors['White'], "Big")
            self.drawText('L to load a map', (960/2-160, 350), self.colors['White'], "Big")
            self.drawText('I to switch to ice tile mode', (960/2-160, 400), self.colors['White'], "Big")
        elif (self.helpText.collidepoint(pygame.mouse.get_pos())):
            self.helpText = self.drawText('How to?', (860, 0), self.colors['Red'], "Big")
        else:
            self.helpText = self.drawText('How to?', (860, 0), self.colors['White'], "Big")
        
    def mainLoop(self):
        while self.running:
            if (time.time() > self.errorTimer + 2):
                self.statusMessage = ''
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): 
                    self.running = False
                    
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_s):
                        self.setSplashScreen()
                        self.errorTimer = time.time()
                        if(self.map.exportMap()):
                            self.statusMessage = "Saving successful!"
                        else:
                            self.statusMessage = "Could not save the map. Make sure you have a player and an exit."
                    elif (event.key == pygame.K_l):
                        self.setSplashScreen()
                        self.errorTimer = time.time()
                        if (self.map.importMap()):
                            self.statusMessage = "Import successful!"
                        else:
                            self.statusMessage = "Could not import the file map.map."
                    elif (event.key == pygame.K_i):
                        self.map.switchMode()
                    elif (event.key == pygame.K_ESCAPE):
                        self.setSplashScreen()
                        self.map.initMap()
                        
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    
                    if (event.button == 1):
                        if (self.helpText.collidepoint(pygame.mouse.get_pos())):
                            self.drawHelp = not self.drawHelp;
                        else:
                            self.map.switchTile(pygame.mouse.get_pos(), False)
                    elif (event.button == 3):
                        self.map.switchTile(pygame.mouse.get_pos(), True)
                        
            self.draw()
            pygame.display.flip()
            self.fpsLimit.tick(60)
        pygame.quit()
    
if __name__ == '__main__':
    window = Editor()
    window.mainLoop()