import pygame

class Level:
    def __init__(self):
        self.setup()
    
    def setup(self):
        self.display_surface = pygame.display.get_surface()
        self.map=pygame.image.load("./assets/map.png").convert_alpha()
    
    def run(self,dt):
        self.display_surface.fill("blue")
        self.display_surface.blit(self.map,(0,0))
        

