import pygame

from src.create_map import Create_map
from screen.Screen_menu import Screen_menu



class Main_screen:
    def __init__(self):
        pygame.init()
        self.game_over = False
        self.game_pause = False
        self.address = 'E'
        self.map_game = Create_map(17,23).maker()

        self.settings()
        Screen_menu(self.game_over, self.game_pause, self.address, self.map_game).menu(self.screen)

    def settings(self):
        self._size = (1042, 810)

        self.screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        
