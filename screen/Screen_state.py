import pygame
from components import Text, Button
from assets.Assets import victory_img
import style.style as st
import assets.Assets as asset


class Screen_state:
    def __init__(self, backgorund, game_over) -> None:
        self._font_game_over = st.font(100)
        self._font_state = st.font(25)
        self._font_pause_menu = st.font(80)
        
        self.background = backgorund
        self.game_over = game_over


    def screen_victory(self, screen, moves):
            
        screen.blit(self.background, (0,0))
        screen.blit(victory_img, victory_img.get_rect(center=(st.SCREEN_WIDTH/2, 250)))
        Text.Text(f'-Movimientos realizados: {moves}-', self._font_state, st.WHITE).draw_text_center(screen,750)
        

        if Button.Button(asset.btn_reset, 1).btn_center(screen, 550):
            return True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game_over = True




    def screen_game_over(self, screen, state = None):
            
        screen.blit(self.background, (0,0))

        Text.Text('Game Over', self._font_game_over, st.WHITE,).draw_text_center(screen, 200)

        if state == '#':
            Text.Text('-Robot destruido-', self._font_state, st.WHITE).draw_text_center(screen, 350)
        else:
            Text.Text('-Movimientos agotados-', self._font_state, st.WHITE).draw_text_center(screen,350)


        if Button.Button(asset.btn_reset, 1).btn_center(screen, 500):
            return True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game_over = True
            
            
    def screen_pause(self, screen):
        screen.blit(self.background, (0,0))
        
        Text.Text('Pause menu', self._font_pause_menu, st.WHITE).draw_text_center(screen, 120)
        
        if Button.Button( asset.btn_continue, 1).btn_center(screen, 380):
            return 'pause'
                
        elif Button.Button( asset.btn_reset, 1).btn_center(screen, 580):
            return 'reset'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game_over = True

    