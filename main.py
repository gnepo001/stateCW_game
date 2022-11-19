import pygame, sys
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920,1080))
        pygame.display.set_caption("Civil War")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() /1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()