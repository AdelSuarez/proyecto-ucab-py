import pygame
class Screen_state:
    def __init__(self, backgorund, asset, game_over, clock) -> None:
        self.background = backgorund
        self._asset = asset
        self._game_over = game_over
        self.clock = clock


    def victory(self, screen):
        while not self._game_over:
            screen.blit(self.background, (0,0))
            screen.blit(self._asset, (150,120))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._game_pause = True
            pygame.display.update()
            self.clock.tick(60)

    def game_over(self, screen):
        while not self._game_over:
            screen.blit(self.background, (0,0))
            screen.blit(self._asset, (220,180))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._game_pause = True
            pygame.display.update()
            self.clock.tick(60)