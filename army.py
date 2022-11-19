import pygame

class Army(pygame.sprite.Sprite):
    def __init__(self,pos,group,size,speed):
        super().__init__(group)
        self.size = size
        self.speed = speed
        self.image = pygame.image.load("./assets/army.png")
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)

        self.direction = pygame.math.Vector2()

    def location(self,toLocationX,toLocationY):
        if self.pos is not (toLocationX,toLocationY):
            if self.pos.x > toLocationX:
                self.direction.x = -1
            elif self.pos.x < toLocationX:
                self.direction.x = 1
            else:
                self.direction.x = 0

            if self.pos.y > toLocationY:
                self.direction.y = -1
            elif self.pos.y < toLocationY:
                self.direction.y = 1
            else:
                self.direction.y = 0
        else:
            self.direction = (0,0)


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
        self.location(200,250)
        self.move(dt)
