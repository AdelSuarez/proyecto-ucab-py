import pygame
import assets.Assets as asset
import style.style as st
from components import Text, Button
from screen.Screen_game import Screen_game



class Screen_menu:
    def __init__(self, game_over) -> None:
        self._font = st.font(100)
        self._font_version = st.font( 20)

        self.game_over = game_over
        self.game_pause = False


    def menu(self, screen):
        while not self.game_over:

            if self.game_pause:
                # Map
                Screen_game(self.game_over, self.game_pause).game(screen)
            else:

                screen.fill((52,78,91))
                # Menu
                Text.Text('ROBOTcok', self._font, st.WHITE).draw_text_center(screen,120)
                Text.Text('BETA', self._font_version, st.RED).draw_text(screen, 850,170)
                Text.Text('v2.7.5.4', self._font_version, st.WHITE).draw_text(screen, 870,780)
                if Button.Button( asset.btn_start, 1.5).btn_center(screen, 400):
                    self.game_pause = True
                elif Button.Button( asset.btn_exit,1).btn_center(screen, 700):
                    pygame.quit()

                    self.game_over = True

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_pause = False
                    
            pygame.display.update()