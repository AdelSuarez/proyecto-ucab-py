import pygame
import style.style as st
import assets.Assets as asset
from src import create_map_screen, move, robot_rotation, collision_checker, positions, create_map, Robot_direction, Read_text, State_txt
from screen import Screen_state
from components import Status_bar


class Screen_game:
    automatic = 0
    reset_map = False
    counter_move = 0
    active_map_txt = False
    
    def __init__(self, game_over, controller, mode_map_txt=None) -> None:
        self._font = st.font(80)
        self._font_bar = st.font(15)
        
        self.controller = controller
        self.game_over = game_over
        self.address = 'E'
        self.background = asset.BG_opacity
        self.pause_active = False
        self.state_active = True
        self.mode_map_txt = mode_map_txt
        (self.map_game_txt, self.moves) = Read_text.Read_text().convert_map()

    def game(self, screen):
        while not self.game_over:

            if self.mode_map_txt is None:
                if not Screen_game.reset_map:
                    self.map_game = create_map.Create_map(17,23).maker()
                    Screen_game.reset_map=True
                    self.address = 'E'
            else:
                self.map_game = self.map_game_txt

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True

                if not self.pause_active and Screen_game.counter_move <= 60:

                    if event.type == pygame.KEYDOWN:
                        if self.mode_map_txt is None:
                        
                        # seleccion del tipo de control
                            if self.controller:    
                                self.controller_sensor(event)
                            
                            else:
                                self.controller_keys(event)

                        if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                            self.pause_active = True

                        elif self.mode_map_txt != None:
                            if Screen_game.automatic == 0:
                                if event.key == pygame.K_a:
                                    
                                    self.automatic_movements()
                                    Screen_game.automatic += 1
                            
            # posiciones en tiempo real de la meta y el robot            
            (self._position_row_goal, self._position_column_goal) = positions.Positions(self.map_game).position_goal()

            screen.fill(st.BLACK) #Background

            
            create_map_screen.Create_map_screen(self.map_game, screen, self.address, self.controller)

            # barra de esta inferior
            Status_bar.Status_bar(self.map_game, Screen_game.counter_move, self.address).bottom_status_bar(screen)

            self.check_events(screen) # verifica si el jugador gano o perdio

            # activa los eventos del menu de pausa
            if self.pause_active and self.state_active:
                value = Screen_state.Screen_state(self.background, self.game_over).screen_pause(screen) 

                if value == 'pause':
                    self.pause_active = False
                    
                elif value == 'reset' and self.mode_map_txt is None:
                    self.pause_active = False
                    Screen_game.reset_map = False
                    Screen_game.counter_move = 0
                
                elif value == 'reset' and self.mode_map_txt == 'txt':
                    self.reset_map_text()
                    self.pause_active = False


            pygame.display.update() # Actualiza la ventana

    
    def check_events(self,screen):
        # Funcion que verifica si el jugador gana o pierde, y reset o continue en la screen
        value = collision_checker.Collision_checker(self.map_game).checker()
        if value == '#' or Screen_game.counter_move > 60:

            self.state_active = False

            reset_game_over = Screen_state.Screen_state(self.background, self.game_over).screen_game_over(screen, value)

            if reset_game_over and self.mode_map_txt is None:
                self.reset_screen_victory()

            elif reset_game_over and self.mode_map_txt == 'txt':
                self.reset_map_text(True)   

            State_txt.State_text(value)
            

        elif  value == '@':

            self.state_active = False

            reset_victory = Screen_state.Screen_state(self.background, self.game_over).screen_victory(screen, Screen_game.counter_move)
            
            if reset_victory and self.mode_map_txt is None:
                self.reset_screen_victory()


            elif reset_victory and self.mode_map_txt == 'txt':
                self.reset_map_text(True)

            State_txt.State_text(value)
    
    def controller_sensor(self, event):
        # Controles a d i que se usan con el sensor 
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
        #Controles awds para moverse libre en todas las direcciones
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
        # Mueve al robot pero solo para awds
        Robot_direction.Robot_direction(address, self.map_game)
        move.Move(address, self.map_game).advance()
        Screen_game.counter_move += 1

    def automatic_movements(self):
        for move in self.moves:
            if move.upper() == 'A':
                self.address = 'O'
                self.avance_keys(self.address)
            elif move.upper() == 'D':
                self.address = 'E'
                self.avance_keys(self.address)
            elif move.upper() == 'S':
                self.address = 'S'
                self.avance_keys(self.address)
            elif move.upper() == 'W':
                self.address = 'N'
                self.avance_keys(self.address)


    def reset_screen_victory(self):
        Screen_game.reset_map = False
        Screen_game.counter_move = 0
        self.state_active = True
    
    def reset_map_text(self, state=None):
        (self.map_game_txt, self.moves) = Read_text.Read_text().convert_map()
        Screen_game.counter_move = 0

        if state:
            self.state_active = True

        Screen_game.automatic = 0