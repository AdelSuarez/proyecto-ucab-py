import pygame
from components.Text import Text
import style.style as st
class Screen_state:
    def __init__(self, backgorund, game_over, asset = None) -> None:
        self._font = pygame.font.Font("assets/font.ttf", 100)
        self.background = backgorund
        self._asset = asset
        self._game_over = game_over


    def victory(self, screen):
        while not self._game_over:
            screen.blit(self.background, (0,0))
            screen.blit(self._asset, (150,120))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True

            pygame.display.update()

    def game_over(self, screen):
        while not self._game_over:
            screen.blit(self.background, (0,0))

            Text('Game Over', self._font, st.WHITE,).draw_text(screen, 80,300)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True

            pygame.display.update()