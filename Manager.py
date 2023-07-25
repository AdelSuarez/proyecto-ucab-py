import pygame
from assets import Assets as asset
import style.style as st
from screen import Screen_game, Screen_start, Screen_controllers, Screen_map_selection


class Manager:
    def __init__(self):
        pygame.init()
        self.game_over = False
        self._font = st.font(100)
        self._font_controller = st.font(60)
        self._font_text = st.font( 20)

        self.screen_controller_active = False
        self.screen_map_selection_active = False
        self._settings()
        self.manager()
    
    def manager(self):
        while not self.game_over:
            self.screen.fill(st.BACKGROUND_COLOR)

            if self.screen_map_selection_active:
                self.mode_map = Screen_map_selection.Screen_map_selection().screen_selection_map(self.screen)

                if self.mode_map == 'random':
                    self.screen_map_selection_active = False
                    self.screen_controller_active = True

                elif self.mode_map == 'txt':
                    Screen_game.Screen_game(self.game_over, False, self.mode_map).game(self.screen)


            elif self.screen_controller_active:
                mode = Screen_controllers.Screen_controllers().screen_controllers(self.screen)

                if mode == 'sensor':
                    self.screen_map_selection_active = False
                    Screen_game.Screen_game(self.game_over, True).game(self.screen)

                elif mode == 'keys':
                    self.screen_map_selection_active = False
                    Screen_game.Screen_game(self.game_over, False).game(self.screen)
                
                elif mode == 'back':
                    self.screen_map_selection_active = True
                    self.screen_controller_active = False
        
            else:
                if Screen_start.Screen_start().screen_start(self.screen):
                    self.screen_map_selection_active= True


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True
            
            pygame.display.update()

    def _settings(self):
        self.screen = pygame.display.set_mode((st.SCREEN_WIDTH, st.SCREEN_HEIGHT))
        pygame.display.set_caption('ROBOTcok')

        # En linux no aparece el icono del juego
        pygame.display.set_icon(asset.icon)