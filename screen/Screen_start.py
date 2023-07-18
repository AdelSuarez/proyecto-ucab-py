import pygame
import assets.Assets as asset
import style.style as st
from components import Text,Button



class Screen_start:
    def __init__(self ) -> None:
        self._font = st.font(100)
        self._font_text = st.font( 20)


    def screen_start(self, screen):
        Text.Text('ROBOTcok', self._font, st.WHITE).draw_text_center(screen,120)
        Text.Text('BETA', self._font_text, st.RED).draw_text(screen, 850,170)
        Text.Text('v2.8.0.1', self._font_text, st.WHITE).draw_text(screen, 870,780)

        if Button.Button( asset.btn_start, 1.5).btn_center(screen, 400):
            return True
        elif Button.Button( asset.btn_exit,1).btn_center(screen, 700):
            pygame.quit()