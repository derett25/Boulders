'''
Created on 24 jun 2013

@author: Linus
'''
import pygame
import Splash
import Player
import Map
import os

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,50) # Code from http://www.pygame.org/wiki/SettingWindowPosition

class Game:
    '''
    @summary: Creates a new game
    '''
    def __init__(self):
        
        self.tilebg = pygame.image.load('sprites/tilebg.png')
        
        self.screen = pygame.display.get_surface()
        
        self.colors = {'Red': (255, 0, 0), 'White': (255, 255, 255), 'Green': (0, 255, 0), 'Blue': (0, 0, 255), 'Black': (0, 0, 0), 'Yellow': (255, 255, 0)}
        
        # Added these here to reduce input lag
        # Font loading slows down game performance A LOT!
        self.textType = {'Normal': pygame.font.SysFont("Candara", 15), 'Big': pygame.font.SysFont("Candara", 25, bold=1)}
        
        self.fpsLimit = pygame.time.Clock()
        
        self.setSplashScreen()
        self.map = Map.Map()
        self.initGame()
        self.helpText = self.drawText('How to?', (860, 0), self.colors['White'], "Big")
        self.running = True
        
    def setSplashScreen(self):
        '''
        @summary: Creates a loading screen
        '''
        self.drawText('Loading...', (30, 900), self.colors['White'], "Big")
        pygame.display.flip()
        
    def drawText(self, text, pos, color, textSize="Normal"):
        '''
        
        @param text: Text to print
        @param pos: Text position
        @param color: Text color
        @param textSize: Size of the text (Normal/Big)
        '''
        textRender = self.textType[textSize].render(text, True, color)
        return self.screen.blit(textRender, (pos))
        
    def initGame(self):
        '''
        @summary: Initializes the game
        '''
        if not(self.map.initMap()):
            pygame.mixer.music.load('sounds/Game Applause.wav')
            pygame.mixer.music.play(loops=0)
            self.won = True
            return False
        
        self.won = False
        self.drawHelp = False
        
        return True
        
    def draw(self):
        '''
        @summary: Handles drawing of game objects
        '''
        if (self.won):
            self.screen.blit(self.tilebg, (0, 0))
            self.drawText("Thank you for playing Boulders!", (320, 480), self.colors['White'], "Big")
        else:
            self.map.draw()
            self.drawText('Current level: '+str(self.map.getCurrentMap()+1), (10, 0), self.colors['White'], "Big")
            if (self.drawHelp):
                self.helpText = self.drawText('How to?', (860, 0), self.colors['Red'], "Big")
                self.drawText('Move around with the arrow keys', (320, 150), self.colors['White'], "Big")
                self.drawText('Reset the level with ESC', (320, 200), self.colors['White'], "Big")
                self.drawText('Touch a boulder to move it', (320, 250), self.colors['White'], "Big")
                self.drawText('Reach the circle to advance a level', (320, 300), self.colors['White'], "Big")
            elif (self.helpText.collidepoint(pygame.mouse.get_pos())):
                self.helpText = self.drawText('How to?', (860, 0), self.colors['Red'], "Big")
            else:
                self.helpText = self.drawText('How to?', (860, 0), self.colors['White'], "Big")
                
    def handleCollisions(self, gameObject):
        '''
        
        @param gameObject: The object being moved
        '''
        
        position = (gameObject.getPos()[0] + gameObject.getDirection()[0], gameObject.getPos()[1] + gameObject.getDirection()[1])
        
        # Saving for temporary use
        direction = gameObject.getDirection()
        
        for boulder in self.map.getBoulders():
            if (boulder.checkCollision(position)):
                
                if (isinstance(gameObject, Player.Player)):
                    gameObject.changeDirection()
                    boulder.setDirection(direction)
                    self.handleCollisions(boulder)
                    
                gameObject.resetDirection()
                return False
            
        if (self.map.getEnd().checkCollision(position)):
            if (isinstance(gameObject, Player.Player)):
                gameObject.resetDirection()
                self.map.advanceMap()
                self.initGame()
                return False
        
        for tile in self.map.getTiles():
            if (tile.checkCollision(position) and not tile.getWalkable()):
                if (isinstance(gameObject, Player.Player)):
                    gameObject.changeDirection()
                gameObject.resetDirection()
                
                return False;
                
            elif (tile.checkCollision(position) and tile.getGlidable()):
                gameObject.setGlide()
                return True;
                
            elif (tile.checkCollision(position) and tile.getWalkable() and gameObject.getGliding()):
                gameObject.resetDirection()
                
                # Last step to surface
                gameObject.setDirection(direction)
                return True;
            
        return True
    
    def handleMovement(self):
        
        # Moves all the MovableObjects
        
        if (self.map.getPlayer().getMoving()):      
            self.map.getPlayer().move()
            return False
        elif (self.map.getPlayer().getGliding()):
            self.handleCollisions(self.map.getPlayer())
            return False
        
        for boulder in self.map.getBoulders():
            if (boulder.getMoving()):
                boulder.move()
                return False
            elif (boulder.getGliding()):
                self.handleCollisions(boulder)
                return False
                
        return True
        
    def mainLoop(self):
        # Main loop that handles game events
        
        while self.running:
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): 
                    self.running = False
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                        # If a mouse button was pressed on the "How to?"-sign we draw the instructions
                        if (self.helpText.collidepoint(pygame.mouse.get_pos())):
                            self.drawHelp = not self.drawHelp
                            
            
            if (self.handleMovement()):
                
                if not(self.won):
                    keys = pygame.key.get_pressed()
                    
                    if (keys[pygame.K_LEFT]):
                        self.map.getPlayer().setDirection((-32, 0))
                        self.handleCollisions(self.map.getPlayer())
                            
                    elif (keys[pygame.K_RIGHT]):
                        self.map.getPlayer().setDirection((32, 0))
                        self.handleCollisions(self.map.getPlayer())
                                
                    elif (keys[pygame.K_UP]):
                        self.map.getPlayer().setDirection((0, -32))
                        self.handleCollisions(self.map.getPlayer())
                                
                    elif (keys[pygame.K_DOWN]):
                        self.map.getPlayer().setDirection((0, 32))
                        self.handleCollisions(self.map.getPlayer())
                                
                    elif (keys[pygame.K_ESCAPE]):
                        self.initGame()
                                       
            self.draw()
            pygame.display.flip()
            self.fpsLimit.tick(60)
            
        pygame.quit()

if __name__ == "__main__":
    WIDTH = 960
    HEIGHT = 960
    
    pygame.init()
    pygame.display.set_icon(pygame.image.load('sprites/boulder.gif'))
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Boulders")
    pygame.mixer.music.load('sounds/Game.wav')
    pygame.mixer.music.play(-1)
    
    splashWindow = Splash.Splash()
    if (splashWindow.mainLoop()):
        window = Game()
        window.mainLoop()