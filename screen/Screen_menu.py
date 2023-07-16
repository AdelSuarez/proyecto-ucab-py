import pygame
import assets.Assets as asset
import style.style as st
from components import Text, Button
from screen.Screen_game import Screen_game



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
                self.screen_controllers(screen)

            elif self.screen_map_selection_active:
                self.screen_selection_map(screen)

                    
            else:
                self.screen_start(screen)
            
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


    def screen_start(self, screen):
        Text.Text('ROBOTcok', self._font, st.WHITE).draw_text_center(screen,120)
        Text.Text('BETA', self._font_text, st.RED).draw_text(screen, 850,170)
        Text.Text('v2.8.0.1', self._font_text, st.WHITE).draw_text(screen, 870,780)

        if Button.Button( asset.btn_start, 1.5).btn_center(screen, 400):
            self.screen_controller_active = True

        elif Button.Button( asset.btn_exit,1).btn_center(screen, 700):
            pygame.quit()
            self.game_over = True

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
            self.screen_controller_active = False
            self.screen_map_selection_active = True
            self.is_controller = 'sensor'
            self.mode_controller = True

        # btn Mode keys    
        elif Button.Button( asset.btn_continue, 1).btn_center(screen, 700, 800):
            self.screen_controller_active = False
            self.screen_map_selection_active = True
            self.is_controller = 'keys'
            self.mode_controller = False


            # Screen_game(self.game_over, self.screen_controller_active, False).game(screen)

    def screen_selection_map(self, screen):
        Text.Text('Map', self._font_controller, st.WHITE).draw_text_center(screen,100)

        if Button.Button( asset.btn_return, 0.5).btn_center(screen, 100, 120):
            self.screen_controller_active = True
            self.screen_map_selection_active = False



        Text.Text('Random Map', self._font_text, st.WHITE).draw_text(screen, 150,300)
        Text.Text('txt Map', self._font_text, st.WHITE).draw_text(screen, 730,300)

        # btn mapas aleatorios
        if Button.Button( asset.btn_start, 0.8).btn_center(screen, 400, 250):
            Screen_game(self.game_over, self.mode_controller).game(screen)

        # btn mapa del txt
        elif Button.Button( asset.btn_start, 0.8).btn_center(screen, 400, 800):
            print('En desarrollo')
            # Screen_game(self.game_over, self.screen_controller_active, self.mode_controller).game(screen)
            

        Text.Text(f'Controller: {self.is_controller}', self._font_text, st.WHITE).draw_text_center(screen,600)
        
            
