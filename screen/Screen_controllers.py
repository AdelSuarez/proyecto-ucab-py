import pygame
import assets.Assets as asset
import style.style as st
from components import Text,Button


class Screen_controllers:
    def __init__(self) -> None:
        self._font_controller = st.font(60)
        self._font_text = st.font( 20)

    def screen_controllers(self, screen):

        Text.Text('Controllers', self._font_controller, st.WHITE).draw_text_center(screen,100)

        Text.Text('SENSOR', self._font_text, st.WHITE).draw_text(screen, 192,200)
        screen.blit(asset.sensor_img, (80,230))
        Text.Text('A D I', self._font_text, st.WHITE).draw_text(screen, 200,590)

        Text.Text('KEYS', self._font_text, st.WHITE).draw_text(screen, 758,200)
        screen.blit(asset.keys_img, (620,230))
        Text.Text('A W D S', self._font_text, st.WHITE).draw_text(screen, 725,590)


        # btn Mode sensor
        if Button.Button( asset.btn_continue, 1).btn_center(screen, 700, 250):
            return 'sensor'
            

        # btn Mode keys    
        elif Button.Button( asset.btn_continue, 1).btn_center(screen, 700, 800):
            return 'keys'
            