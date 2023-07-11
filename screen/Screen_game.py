import pygame
import style.style as st
import assets.Assets as asset
from src import move, robot_rotation, collision_checker, positions, create_map
from screen import create_map_screen, Screen_state
from components import Text, Button


class Screen_game:
    is_pause = 1
    reset_map = False
    counter_move = 0
    
    def __init__(self, game_over, game_pause) -> None:
        self._font = st.font(15)
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
            self.bar_state(screen)

            if collision_checker.Collision_checker(self.map_game).checker() == '#' or Screen_game.counter_move == 60:
                if Screen_game.reset_map:
                    Screen_state.Screen_state(self.background, self.game_over).screen_game_over(screen, collision_checker.Collision_checker(self.map_game).checker())

            elif  collision_checker.Collision_checker(self.map_game).checker() == '@':
                Screen_state.Screen_state(self.background, self.game_over).screen_victory(screen, Screen_game.counter_move)
            
            if self.pause_active:
                self.screen_pause(screen)




            pygame.display.update()
                

    def bar_state(self,screen):
        # ----------------------Movements----------------------------------
        (self._position_row_robot, self._position_column_robot, self._robot) = positions.Positions(self.map_game).position_robot()
        Text.Text('Movements: ', self._font, st.WHITE).draw_text(screen, 60,780)
        Text.Text(f'{Screen_game.counter_move} ', self._font, st.GREEN_ROBOT).draw_text(screen, 215,780)

        # ----------------------Address----------------------------------
        Text.Text('Address: ', self._font, st.WHITE).draw_text(screen, 300,780)
        Text.Text(f'{self.address} ', self._font, st.GREEN_ROBOT).draw_text(screen, 427,780)

        # ----------------------Robot----------------------------------
        Text.Text('Robot:', self._font, st.WHITE).draw_text(screen, 520,780)
        Text.Text(f'{self._position_row_robot} | {self._position_column_robot}', self._font, st.GREEN_ROBOT).draw_text(screen, 610,780)

        # ----------------------Goal----------------------------------
        Text.Text('Goal:', self._font, st.WHITE).draw_text(screen, 750,780)
        Text.Text(f'{self._position_row_goal} | {self._position_column_goal}', self._font, st.GREEN_ROBOT).draw_text(screen, 825,780)

        # ----------------------Origin Robot----------------------------------
        Text.Text(f'{self._robot}', self._font, st.RED_ROBOT).draw_text(screen, 1000,780)

    def screen_pause(self, screen):
            screen.blit(self.background, (0,0))
            
            # screen.fill(st.BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True
            
            if Button.Button(300, 300, asset.btn_start, 1.5).draw(screen):

                    self.pause_active = False
                    
            elif Button.Button(300, 500, asset.btn_exit, 1.5).draw(screen):

                    self.pause_active = False
                    Screen_game.reset_map = False

        
