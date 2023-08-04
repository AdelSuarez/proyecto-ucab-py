import pygame
import time
import style.style as st
import assets.Assets as asset
from src import create_map_screen, move, robot_rotation, collision_checker, positions, create_map, Robot_direction, Read_txt, State_txt
from . import Screen_state
from components import Status_bar


class ScreenGame:
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
        self.counter_move = 0
        (self.map_game_txt, self.moves) = Read_txt.ReadText().convert_map()

    def game(self, screen):
        while not self.game_over:

            if self.mode_map_txt is None:
                if not ScreenGame.reset_map:
                    self.map_game = create_map.CreateMap(17,23).maker()
                    ScreenGame.reset_map=True
                    self.address = 'E'
            else:
                self.map_game = self.map_game_txt

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True

                if not self.pause_active and ScreenGame.counter_move <= 60:

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
                            if ScreenGame.automatic == 0:
                                if event.key == pygame.K_a:
                                    
                                    ScreenGame.automatic += 1
                                    
                            
            # posiciones en tiempo real de la meta y el robot            
            (self._position_row_goal, self._position_column_goal) = positions.Positions(self.map_game).position_goal()

            screen.fill(st.BLACK) #Background

            
            create_map_screen.CreateMapScreen(self.map_game, screen, self.address, self.controller)

            # barra de esta inferior
            Status_bar.StatusBar(self.map_game, ScreenGame.counter_move, self.address).bottom_status_bar(screen)

            self.check_events(screen) # verifica si el jugador gano o perdio

            # activa los eventos del menu de pausa
            if self.pause_active and self.state_active:
                value = Screen_state.ScreenState(self.background, self.game_over).screen_pause(screen) 

                if value == 'pause':
                    self.pause_active = False
                    
                elif value == 'reset' and self.mode_map_txt is None:
                    self.pause_active = False
                    ScreenGame.reset_map = False
                    ScreenGame.counter_move = 0
                
                elif value == 'reset' and self.mode_map_txt == 'txt':
                    self.reset_map_text()
                    self.pause_active = False

            if ScreenGame.automatic:
                self.automatic_movements()
                time.sleep(0.5)


            pygame.display.update() # Actualiza la ventana

    
    def check_events(self,screen):
        # Funcion que verifica si el jugador gana o pierde, y reset o continue en la screen
        value = collision_checker.CollisionChecker(self.map_game).checker()
        if value == '#' or ScreenGame.counter_move > 60:

            self.state_active = False

            reset_game_over = Screen_state.ScreenState(self.background, self.game_over).screen_game_over(screen, value)

            if reset_game_over and self.mode_map_txt is None:
                self.reset_screen_victory()

            elif reset_game_over and self.mode_map_txt == 'txt':
                self.reset_map_text(True)   

            State_txt.StateText(value)
            

        elif  value == '@':

            self.state_active = False

            reset_victory = Screen_state.ScreenState(self.background, self.game_over).screen_victory(screen, ScreenGame.counter_move)
            
            if reset_victory and self.mode_map_txt is None:
                self.reset_screen_victory()


            elif reset_victory and self.mode_map_txt == 'txt':
                self.reset_map_text(True)

            State_txt.StateText(value)
    
    def controller_sensor(self, event):
        # Controles a d i que se usan con el sensor 
        if event.key == pygame.K_a:
            move.Move(self.address, self.map_game).advance()
            ScreenGame.counter_move += 1

        elif event.key == pygame.K_d:
            self.address = robot_rotation.RobotRotation(self.address, self.map_game).right()
            ScreenGame.counter_move += 1

        elif event.key == pygame.K_i:
            self.address = robot_rotation.RobotRotation(self.address, self.map_game).left()
            ScreenGame.counter_move += 1
            
        elif event.key == pygame.K_q:
            ScreenGame.reset_map=False


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
        Robot_direction.RobotDirection(address, self.map_game)
        move.Move(address, self.map_game).advance()
        ScreenGame.counter_move += 1

    def automatic_movements(self):
            try:
                move = self.moves[self.counter_move]
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
                self.counter_move += 1
            except Exception:
                self.counter_move = 0
                ScreenGame.automatic = 0



    def reset_screen_victory(self):
        ScreenGame.reset_map = False
        ScreenGame.counter_move = 0
        self.state_active = True

    
    def reset_map_text(self, state=None):
        (self.map_game_txt, self.moves) = Read_txt.ReadText().convert_map()
        ScreenGame.counter_move = 0

        if state:
            self.state_active = True

        ScreenGame.automatic = 0