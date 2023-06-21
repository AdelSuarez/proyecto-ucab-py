try:
    from getch import getche
except ModuleNotFoundError:
    pass

from src.archivo import Archivo
from cmd.welcome import Data_map
from src.create_map import Create_map
from cmd.view_map import View_map
import style.style as st
from src.clear_terminal import clear
from cmd.positions import Positions
from cmd.robot_rotation import Robot_rotation
from cmd.move import Move
from cmd.collision_checker import Collision_checker
from cmd.end_game import End_game

class Main_menu:
    order_counter = 0
    movement = ''

    def __init__(self):
        self._row, self._column = Data_map().welcome()
        self.map_game = Create_map(self._row, self._column).maker()
        self._position_row_g, self._position_column_g = Positions(self.map_game).position_goal()
        self.address = 'E'
        self._menu()
        


    def _menu(self):
        while True:
            clear()
            position_row_r, position_column_r = Positions(self.map_game).position_robot()

            Archivo(self._row, self._column, self.map_game, position_row_r, position_column_r, self._position_row_g, self._position_column_g, self.address, Main_menu.order_counter, Main_menu.movement, Collision_checker(self.map_game).checker())


            print(f' C: {self._column} | F: {self._row} '.center((self._column*4)+3,'-'))   

            print('')
            View_map(self._column, self.map_game).view()
            print('')

            self._positions(position_column_r, position_row_r)
            self._controllers()

            
            if Main_menu.order_counter > 40:
                End_game(Main_menu.order_counter, Collision_checker(self.map_game).checker(), self._column, self.map_game)
                break

            if Collision_checker(self.map_game).checker() == '#' or Collision_checker(self.map_game).checker() == '@':
                End_game(Main_menu.order_counter, Collision_checker(self.map_game).checker(), self._column, self.map_game)
                break


            try:
                # Linux
                motion = getche()
            except Exception:
                # Windows
                motion = input(f'Introduce el movimiento {st.GREEN}>>{st.RESET} ')


            if motion.lower().strip() == 'i':
                Main_menu.order_counter +=1
                Main_menu.movement += 'I'
                self.address = Robot_rotation(self.address, self.map_game).left()

            elif motion.lower().strip() == 'd':
                Main_menu.order_counter +=1
                Main_menu.movement += 'D'
                self.address = Robot_rotation(self.address, self.map_game).right()


            elif motion.lower().strip() == 'a':
                Main_menu.order_counter +=1
                Main_menu.movement += 'A'
                Move(self.address, self.map_game).advance()



    def _positions(self, position_column_r, position_row_r):
        print('Posiciones'.center((self._column*4)+3, '-'))
        print(f'° Robot {st.GREEN}>>{st.RESET} C: {st.BLUE}{position_column_r}{st.RESET} | F: {st.BLUE}{position_row_r}{st.RESET}\n° Meta  {st.GREEN}>>{st.RESET} C: {st.BLUE}{self._position_column_g}{st.RESET} | F: {st.BLUE}{self._position_row_g}{st.RESET} \n{st.CYAN}v1.9.0.1{st.RESET}')

    def _controllers(self):
        print(f'''
    N     | Ordenes: {st.BLUE}{Main_menu.order_counter}{st.RESET}
    ↑     ---------------------------    
O ← {st.GREEN}{self.address}{st.RESET} → E | A {st.GREEN}>>{st.RESET} Avanzar
    ↓     | I {st.GREEN}>>{st.RESET} Mover a la Izquierda
    S     | D {st.GREEN}>>{st.RESET} Mover a la Derecha
''')