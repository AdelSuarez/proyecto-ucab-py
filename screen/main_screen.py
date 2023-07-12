import pygame
from assets import Assets as asset
from screen.Screen_menu import Screen_menu
import style.style as st

class Main_screen:
    def __init__(self):
        pygame.init()
        self.game_over = False


        self.settings()
        Screen_menu(self.game_over).menu(self.screen)

    def settings(self):
        self._size = (st.SCREEN_WIDTH, st.SCREEN_HEIGHT)

        self.screen = pygame.display.set_mode(self._size)
        
        pygame.display.set_caption('ROBOTcok')

        # En linux no aparece el icono del juego
        pygame.display.set_icon(asset.icon)

        
