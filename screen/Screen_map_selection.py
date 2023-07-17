import pygame
import assets.Assets as asset
import style.style as st
from screen import Screen_game
from components import Text,Button


class Screen_map_selection:
    def __init__(self, game_over, mode_controller, is_controller) -> None:
        self._font_controller = st.font(60)
        self._font_text = st.font( 20)
        self.game_over = game_over
        self.mode_controller = mode_controller
        self.is_controller = is_controller


    def screen_selection_map(self, screen):
        Text.Text('Map', self._font_controller, st.WHITE).draw_text_center(screen,100)

        if Button.Button( asset.btn_return, 0.5).btn_center(screen, 100, 120):
            return True



        Text.Text('Random Map', self._font_text, st.WHITE).draw_text(screen, 150,300)
        Text.Text('txt Map', self._font_text, st.WHITE).draw_text(screen, 730,300)

        # btn mapas aleatorios
        if Button.Button( asset.btn_start, 0.8).btn_center(screen, 400, 250):
            Screen_game.Screen_game(self.game_over, self.mode_controller).game(screen)

        # btn mapa del txt
        elif Button.Button( asset.btn_start, 0.8).btn_center(screen, 400, 800):
            print('En desarrollo')
            # Screen_game(self.game_over, self.screen_controller_active, self.mode_controller).game(screen)
            

        Text.Text(f'Controller: {self.is_controller}', self._font_text, st.WHITE).draw_text_center(screen,600)