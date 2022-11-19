import pygame
from camera import CrosshairCamera
from sprites import quickCreate
from army import Army
from state import States

class Level:
    def __init__(self):

        #create sprite group to easily render/update/animate all sprites
        self.all_sprites = CameraGroup()
        self.setup()
    
    def setup(self):
        self.display_surface = pygame.display.get_surface()
        #load map
        quickCreate(pos=(0,0),surf=pygame.image.load('./assets/map.png').convert_alpha(),groups=self.all_sprites)
        states = States(group=self.all_sprites)
        
        #set player to camera 
        self.army1 = Army((1000,1000),self.all_sprites,50,100)
        self.player = CrosshairCamera((1000,1000),self.all_sprites)
    
    def run(self,dt):
        self.display_surface.fill("blue")
        #draw and update all sprites
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
       
       
#off set sprites to camera movement
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()


    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - 1920/2
        self.offset.y = player.rect.centery - 1080/2
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image,offset_rect)