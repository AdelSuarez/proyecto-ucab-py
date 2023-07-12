import pygame
import style.style as st
import assets.Assets as asset
from src import move, robot_rotation, collision_checker, positions, create_map
from screen import create_map_screen, Screen_state
from components import Text, Button, Status_bar


class Screen_game:
    is_pause = 1
    reset_map = False
    counter_move = 0
    
    def __init__(self, game_over, game_pause) -> None:
        self._font = st.font(80)

        self._font_bar = st.font(15)
        self.game_over = game_over
        self.address = 'E'
        self.game_pause = game_pause
        self.background = asset.BG_opacity
        self.pause_active = False

    def game(self, screen):
        while not self.game_over:
            if not Screen_game.reset_map:

                self.map_game = create_map.Create_map(17,23).maker()
                Screen_game.reset_map=True
                self.address = 'E'

            (self._position_row_goal, self._position_column_goal) = positions.Positions(self.map_game).position_goal()
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True

                if not self.pause_active:

                    if event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_a:
                            move.Move(self.address, self.map_game).advance()
                            Screen_game.counter_move += 1

                        elif event.key == pygame.K_d:
                            self.address = robot_rotation.Robot_rotation(self.address, self.map_game).right()
                            Screen_game.counter_move += 1

                        elif event.key == pygame.K_i:
                            self.address = robot_rotation.Robot_rotation(self.address, self.map_game).left()
                            Screen_game.counter_move += 1
                            
                        elif event.key == pygame.K_q:
                            Screen_game.reset_map=False

                        if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                            self.pause_active = True

                        

            screen.fill(st.BLACK)

            
            create_map_screen.Create_map_screen(self.map_game, screen, asset.robot, self.address, asset.bomb, asset.goal, asset.victory, asset.over)

            # barra de esta inferior
            Status_bar.Status_bar(self.map_game, Screen_game.counter_move, self.address).bottom_status_bar(screen)

            if collision_checker.Collision_checker(self.map_game).checker() == '#' or Screen_game.counter_move == 60:
                if Screen_game.reset_map:
                    Screen_state.Screen_state(self.background, self.game_over).screen_game_over(screen, collision_checker.Collision_checker(self.map_game).checker())

            elif  collision_checker.Collision_checker(self.map_game).checker() == '@':
                Screen_state.Screen_state(self.background, self.game_over).screen_victory(screen, Screen_game.counter_move)
            
            if self.pause_active:
                self.screen_pause(screen)

            pygame.display.update()
                

    def screen_pause(self, screen):
            screen.blit(self.background, (0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True

            Text.Text('Pause menu', self._font, st.WHITE).draw_text_center(screen, 100)
            if Button.Button( asset.btn_start, 1.5).btn_center(screen, 300):

                    self.pause_active = False
                    
            elif Button.Button( asset.btn_reset, 1).btn_center(screen, 500):

                    self.pause_active = False
                    Screen_game.reset_map = False

        
