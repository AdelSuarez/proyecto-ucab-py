import pygame
import style.style as st
import assets.Assets as asset
from src import create_map_screen, move, robot_rotation, collision_checker, positions, create_map, Robot_direction
from screen import Screen_state
from components import Status_bar


class Screen_game:
    is_pause = 1
    reset_map = False
    counter_move = 0
    
    def __init__(self, game_over, game_pause, controller) -> None:
        self._font = st.font(80)

        self._font_bar = st.font(15)
        self.controller = controller
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

                        if self.controller:    
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
                        
                        else:
                            
                            if event.key == pygame.K_w or event.key == pygame.K_UP:
                                self.address = 'N'
                                Robot_direction.Robot_direction(self.address, self.map_game)
                                move.Move(self.address, self.map_game).advance()
                                Screen_game.counter_move += 1

                            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                self.address = 'S'
                                Robot_direction.Robot_direction(self.address, self.map_game)
                                move.Move(self.address, self.map_game).advance()
                                Screen_game.counter_move += 1

                            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                self.address = 'O'
                                Robot_direction.Robot_direction(self.address, self.map_game)
                                move.Move(self.address, self.map_game).advance()
                                Screen_game.counter_move += 1
                                
                            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                self.address = 'E'
                                Robot_direction.Robot_direction(self.address, self.map_game)
                                move.Move(self.address, self.map_game).advance()
                                Screen_game.counter_move += 1

                            if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                                self.pause_active = True
                            
                        

            screen.fill(st.BLACK)

            
            create_map_screen.Create_map_screen(self.map_game, screen, self.address, self.controller)

            # barra de esta inferior
            Status_bar.Status_bar(self.map_game, Screen_game.counter_move, self.address).bottom_status_bar(screen)

            # verifica si el jugador gano o perdio
            self.check_events(screen)

            # activa los eventos del menu de pausa
            if self.pause_active:
                value = Screen_state.Screen_state(self.background, self.game_over).screen_pause(screen) 
                if value == 'pause':
                    self.pause_active = False
                elif value == 'reset':
                    self.pause_active = False
                    Screen_game.reset_map = False
                     

            pygame.display.update()

    
    def check_events(self,screen):
        if collision_checker.Collision_checker(self.map_game).checker() == '#' or Screen_game.counter_move == 60:

            if Screen_state.Screen_state(self.background, self.game_over).screen_game_over(screen, collision_checker.Collision_checker(self.map_game).checker()):
                
                Screen_game.reset_map = False
                Screen_game.counter_move = 0
                    

        elif  collision_checker.Collision_checker(self.map_game).checker() == '@':
            
            if Screen_state.Screen_state(self.background, self.game_over).screen_victory(screen, Screen_game.counter_move):
                
                Screen_game.reset_map = False
                Screen_game.counter_move = 0
                

        
