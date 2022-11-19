import pygame

class CrosshairCamera(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load("./assets/crosshair.png")
        self.rect = self.image.get_rect(center=pos)
        self.visible = True

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 400

    def input(self,):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
                self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_c]:
            print(self.pos.x,self.pos.y)

    def move(self,dt):
        #normilizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        #vertical movement
        self.pos.y += self.direction.y * self.speed *dt 
        self.rect.centery = self.pos.y

    def update(self,dt):
        self.input()
        self.move(dt)