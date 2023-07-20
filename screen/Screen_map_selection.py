import pygame
import assets.Assets as asset
import style.style as st
from components import Text,Button


class Screen_map_selection:
    def __init__(self) -> None:
        self._font_controller = st.font(60)
        self._font_text_title = st.font(20)
        self._font_text = st.font(10)

    def screen_selection_map(self, screen):
        Text.Text('Map', self._font_controller, st.WHITE).draw_text_center(screen,100)

        Text.Text('Random Map', self._font_text_title, st.WHITE).draw_text(screen, 150,300)
        Text.Text('txt Map', self._font_text_title, st.WHITE).draw_text(screen, 730,300)



        # btn mapas aleatorios
        if Button.Button( asset.btn_start, 0.8).btn_center(screen, 400, 250):
            return 'random'

        # btn mapa del txt
        elif Button.Button( asset.btn_start, 0.8).btn_center(screen, 400, 800):
            return 'txt'
            
        Text.Text('press "a" for automatic mode', self._font_text, st.WHITE).draw_text(screen, 670,500)
            

        Text.Text('the txt map can not be used the keys, it is only to show the result of the data', self._font_text, st.WHITE).draw_text_center(screen,700)