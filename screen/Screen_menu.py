import pygame
import style.style as st
from screen import Screen_game, Screen_start, Screen_controllers, Screen_map_selection


class Screen_menu:
    def __init__(self, game_over: bool) -> None:
        self._font = st.font(100)
        self._font_controller = st.font(60)
        self._font_text = st.font(20)

        self.game_over: bool = game_over
        self.screen_controller_active: bool = False
        self.screen_map_selection_active: bool = False

    def menu(self, screen):
        while not self.game_over:
            screen.fill(st.BACKGROUND_COLOR)

            if self.screen_map_selection_active:
                self.mode_map = Screen_map_selection.Screen_map_selection().screen_selection_map(screen)

                if self.mode_map == 'random':
                    self.screen_map_selection_active = False
                    self.screen_controller_active = True

                elif self.mode_map == 'txt':
                    Screen_game.Screen_game(
                        self.game_over, False, self.mode_map).game(screen)

            elif self.screen_controller_active:
                mode = Screen_controllers.Screen_controllers().screen_controllers(screen)

                if mode == 'sensor':
                    self.screen_map_selection_active = False
                    Screen_game.Screen_game(self.game_over, True).game(screen)

                elif mode == 'keys':
                    self.screen_map_selection_active = False
                    Screen_game.Screen_game(self.game_over, False).game(screen)

                elif mode == 'back':
                    self.screen_map_selection_active = True
                    self.screen_controller_active = False

            else:
                if Screen_start.Screen_start().screen_start(screen):
                    self.screen_map_selection_active = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True

            pygame.display.update()
