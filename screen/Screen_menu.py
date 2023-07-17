import pygame
import assets.Assets as asset
import style.style as st
from components import Text, Button
from screen import Screen_game, Screen_start, Screen_controllers, Screen_map_selection



class Screen_menu:
    def __init__(self, game_over) -> None:
        self._font = st.font(100)
        self._font_controller = st.font(60)
        self._font_text = st.font( 20)

        self.game_over = game_over
        self.screen_controller_active = False
        self.screen_map_selection_active = False
        self.is_controller = ''
        self.mode_controller = None


    def menu(self, screen):
        while not self.game_over:
            screen.fill(st.BACKGROUND_COLOR)

            if self.screen_controller_active:

                mode = Screen_controllers.Screen_controllers().screen_controllers(screen)

                if mode == 'sensor':
                    self.screen_controller_active = False
                    self.screen_map_selection_active = True
                    self.is_controller = 'sensor'
                    self.mode_controller = True

                elif mode == 'keys':
                    self.screen_controller_active = False
                    self.screen_map_selection_active = True
                    self.is_controller = 'keys'
                    self.mode_controller = False

                # self.screen_controllers(screen)

            elif self.screen_map_selection_active:
                back = Screen_map_selection.Screen_map_selection(self.game_over, self.mode_controller, self.is_controller).screen_selection_map(screen)
                
                if back:
                    self.screen_controller_active = True
                    self.screen_map_selection_active = False
                
                    
            else:
                if Screen_start.Screen_start( self.screen_controller_active).screen_start(screen):
                    self.screen_controller_active= True
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True

                # if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    # pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.screen_controller_active = False
                    
            pygame.display.update()


        
            
