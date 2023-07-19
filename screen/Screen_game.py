import pygame
import style.style as st
import assets.Assets as asset
from src import create_map_screen, move, robot_rotation, collision_checker, positions, create_map, Robot_direction
from screen import Screen_state
from components import Status_bar


class Screen_game:
    automatic = 0
    reset_map = False
    counter_move = 0
    
    def __init__(self, game_over, controller, game_map_txt=None, moves = None) -> None:
        self._font = st.font(80)
        self._font_bar = st.font(15)
        
        self.controller = controller
        self.game_over = game_over
        self.address = 'E'
        self.background = asset.BG_opacity
        self.pause_active = False
        self.state_active = True
        self.game_map_txt = game_map_txt
        self.moves = moves

    def game(self, screen):
        while not self.game_over:

            if self.game_map_txt is None:
                if not Screen_game.reset_map:
                    self.map_game = create_map.Create_map(17,23).maker()
                    Screen_game.reset_map=True
                    self.address = 'E'
            else:
                self.map_game = self.game_map_txt

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True

                if not self.pause_active and Screen_game.counter_move <= 60:

                    if event.type == pygame.KEYDOWN:
                        if self.game_map_txt is None:
                        
                        # seleccion del tipo de control
                            if self.controller:    
                                self.controller_sensor(event)
                            
                            else:
                                self.controller_keys(event)

                            if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                                self.pause_active = True

                        elif self.game_map_txt != None:
                            if Screen_game.automatic == 0:
                                if event.key == pygame.K_SPACE:
                                    
                                    self.automatic_movements()
                                    Screen_game.automatic += 1
                            
            # posiciones en tiempo real de la meta y el robot            
            (self._position_row_goal, self._position_column_goal) = positions.Positions(self.map_game).position_goal()

            screen.fill(st.BLACK)

            
            create_map_screen.Create_map_screen(self.map_game, screen, self.address, self.controller)

            # barra de esta inferior
            Status_bar.Status_bar(self.map_game, Screen_game.counter_move, self.address).bottom_status_bar(screen)

            # verifica si el jugador gano o perdio
            self.check_events(screen)

            # activa los eventos del menu de pausa
            if self.pause_active and self.state_active:
                value = Screen_state.Screen_state(self.background, self.game_over, self.game_map_txt).screen_pause(screen) 

                if value == 'pause':
                    self.pause_active = False
                    
                elif value == 'reset':
                    self.pause_active = False
                    Screen_game.reset_map = False
                    Screen_game.counter_move = 0

                     

            pygame.display.update()

    
    def check_events(self,screen):
        if collision_checker.Collision_checker(self.map_game).checker() == '#' or Screen_game.counter_move > 60:

            self.state_active = False

            if Screen_state.Screen_state(self.background, self.game_over, self.game_map_txt).screen_game_over(screen, collision_checker.Collision_checker(self.map_game).checker()):
                
                Screen_game.reset_map = False
                Screen_game.counter_move = 0
                self.state_active = True

        elif  collision_checker.Collision_checker(self.map_game).checker() == '@':

            self.state_active = False
            
            if Screen_state.Screen_state(self.background, self.game_over, self.game_map_txt).screen_victory(screen, Screen_game.counter_move):
                
                Screen_game.reset_map = False
                Screen_game.counter_move = 0
                self.state_active = True
    
    def controller_sensor(self, event):
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


    def controller_keys(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.address = 'N'
            self.avance_keys(self.address)

        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.address = 'S'
            self.avance_keys(self.address)


        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.address = 'O'
            self.avance_keys(self.address)

            
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.address = 'E'
            self.avance_keys(self.address)


    def avance_keys(self, address):
        Robot_direction.Robot_direction(address, self.map_game)
        move.Move(address, self.map_game).advance()
        Screen_game.counter_move += 1

    def automatic_movements(self):
        print(self.moves)
        for move in self.moves:
            if move == 'A':
                self.address = 'O'
                self.avance_keys(self.address)
            elif move == 'D':
                self.address = 'E'
                self.avance_keys(self.address)
            elif move == 'S':
                self.address = 'S'
                self.avance_keys(self.address)
            elif move == 'W':
                self.address = 'N'
                self.avance_keys(self.address)
