import pygame
from components.Text import Text
from assets.Assets import victory_img
import style.style as st


class Screen_state:
    def __init__(self, backgorund, game_over) -> None:
        self._font = st.font(100)
        self._font_state = st.font(25)

        self.background = backgorund
        self.game_over = game_over


    def screen_victory(self, screen, moves):
            screen.blit(self.background, (0,0))
            screen.blit(victory_img, (150,120))
            # Text(f'-Movimientos realizados: {moves}-', self._font_state, st.WHITE).draw_text(screen, 180,530)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True


    def screen_game_over(self, screen,  state = None):
            screen.blit(self.background, (0,0))

            Text('Game Over', self._font, st.WHITE,).draw_text(screen, 80,300)

            if state == '#':
                Text('-Robot destruido-', self._font_state, st.WHITE).draw_text(screen, 300,450)
            else:
                Text('-Movimientos agotados-', self._font_state, st.WHITE).draw_text(screen, 230,450)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True



    