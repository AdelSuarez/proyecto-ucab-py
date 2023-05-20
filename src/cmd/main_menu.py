from src.cmd.data_map import Data_map
from src.cmd.create_map import Create_map
from src.cmd.view_map import View_map
import style.style as st
from src.cmd.clear_terminal import clear
from src.cmd.positions import Positions
from src.cmd.robot_rotation import Robot_rotation
from src.cmd.move import Move
from src.cmd.collision_checker import Collision_checker
from src.cmd.end_game import End_game

class Main_menu:
    order_counter = 0


    def __init__(self):
        self._row, self._column = Data_map().welcome()
        self.map_game = Create_map(self._row, self._column).maker()
        self._position_row_g, self._position_column_g = Positions(self.map_game).position_goal()
        self.address = 'E'
        self.menu()
        


    def menu(self):
        while True:
            clear()
            position_row_r, position_column_r = Positions(self.map_game).position_robot()


            print(f' C: {self._column} | F: {self._row} '.center((self._column*4)+3,'-'))   

            print('')
            View_map(self._column, self.map_game).view()
            print('')
            print('Posiciones'.center((self._column*4)+3, '-'))

            print(f'° Robot {st.GREEN}>>{st.RESET} C: {st.BLUE}{position_column_r}{st.RESET} | F: {st.BLUE}{position_row_r}{st.RESET}\n° Meta  {st.GREEN}>>{st.RESET} C: {st.BLUE}{self._position_column_g}{st.RESET} | F: {st.BLUE}{self._position_row_g}{st.RESET} \n{st.CYAN}v1.1.0.5{st.RESET}')

            print(f'''
    N     | Ordenes: {st.BLUE}{Main_menu.order_counter}{st.RESET}
    ↑     ---------------------------    
O ← {st.GREEN}{self.address}{st.RESET} → E | A {st.GREEN}>>{st.RESET} Avanzar
    ↓     | I {st.GREEN}>>{st.RESET} Mover a la Izquierda
    S     | D {st.GREEN}>>{st.RESET} Mover a la Derecha
''')
            
            if Main_menu.order_counter > 40:
                End_game(Main_menu.order_counter, Collision_checker(self.map_game).checker(), self._column, self.map_game)
                break

            if Collision_checker(self.map_game).checker() == '#' or Collision_checker(self.map_game).checker() == '@':
                End_game(Main_menu.order_counter, Collision_checker(self.map_game).checker(), self._column, self.map_game)
                break
            
            motion = input(f'Introduce el movimiento {st.GREEN}>>{st.RESET} ')

            if motion.lower().strip() == 'i':
                Main_menu.order_counter +=1
                self.address = Robot_rotation(self.address, self.map_game).left()

            elif motion.lower().strip() == 'd':
                Main_menu.order_counter +=1
                self.address = Robot_rotation(self.address, self.map_game).right()


            elif motion.lower().strip() == 'a':
                Main_menu.order_counter +=1
                Move(self.address, self.map_game).advance()
