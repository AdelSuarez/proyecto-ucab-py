from src.cmd.data_map import Data_map
from src.cmd.create_map import Create_map
from src.cmd.view_map import View_map
import style.style as st
from src.cmd.clear_terminal import clear
from src.cmd.positions import Positions

class Main_menu:
    order_counter = 0


    def __init__(self):
        self._row, self._column = Data_map().welcome()
        self.map_game = Create_map(self._row, self._column).maker()
        self._position_row_g, self._position_column_g = Positions(self.map_game).position_goal()
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

            print(f'° Robot {st.GREEN}>>{st.RESET} C: {st.BLUE}{position_column_r}{st.RESET} | F: {st.BLUE}{position_row_r}{st.RESET}\n° Meta  {st.GREEN}>>{st.RESET} C: {st.BLUE}{self._position_column_g}{st.RESET} | F: {st.BLUE}{self._position_row_g}{st.RESET} \n{st.CYAN}v1.0.7{st.RESET}')

            print(f'''
    N     | Ordenes: {st.BLUE}{Main_menu.order_counter}{st.RESET}
    ↑     ---------------------------    
O ← {st.GREEN}{'e'}{st.RESET} → E | A {st.GREEN}>>{st.RESET} Avanzar
    ↓     | I {st.GREEN}>>{st.RESET} Mover a la Izquierda
    S     | D {st.GREEN}>>{st.RESET} Mover a la Derecha
''')
            movimiento = input(f'Introduce el movimiento {st.GREEN}>>{st.RESET} ')






# def Manager():

#     # Variables 
#     # direccion = 'E'
#     # contador_ordenes = 0

#     (y, x) =  datos_mapa()
#     crear_mapa(x, y)
#     verificador_mapa(y, x)
#     # crear_archivo(x, y, mapa)

#     # (posicion_y_m, posicion_x_m) = posicion_meta()
    
#     while True:


#         (posicion_x_r, posicion_y_r) = posicion_robot()
#         limpiar_consola()

#         print(f' C: {y} | F: {x} '.center((y*4)+3,'-'))
#         print('')
#         mostrar_mapa(y)
#         print('')
#         print('Posiciones'.center((y*4)+3, '-'))
#         print(f'° Robot {verde}>>{resetear} C: {azul}{posicion_x_r}{resetear} | F: {azul}{posicion_y_r}{resetear}\n° Meta  {verde}>>{resetear} C: {azul}{posicion_x_m}{resetear} | F: {azul}{posicion_y_m}{resetear} \n{cian}v1.0.7{resetear}')
        
#         print(f'''
#     N     | Ordenes: {azul}{contador_ordenes}{resetear}
#     ↑     ---------------------------    
# O ← {verde}{direccion}{resetear} → E | A {verde}>>{resetear} Avanzar
#     ↓     | I {verde}>>{resetear} Mover a la Izquierda
#     S     | D {verde}>>{resetear} Mover a la Derecha
# ''')
        
#         # # ! Cierra el ciclo principal debido a que supero las ordenes extablecidas
#         # if contador_ordenes > 40:
#         #     fin_juego(contador_ordenes, verificador_colision(), y)
#         #     break
#         # # ! Cierra el ciclo principal debido a que el robot perdio
#         # if verificador_colision() == '#' or verificador_colision() == '@' :
#         #     fin_juego(contador_ordenes, verificador_colision(), y)
#         #     break

#         movimiento = input(f'Introduce el movimiento {verde}>>{resetear} ')

#         # # * Condicional que realiza el cambio de la direccion del robot en el mapa 
#         # if movimiento.lower().strip() == 'i':
#         #     contador_ordenes +=1
#         #     direccion = mover_robot_izquierda(direccion)

#         # elif movimiento.lower().strip() == 'd':
#         #     contador_ordenes +=1
#         #     direccion = mover_robot_derecha(direccion)

#         # elif movimiento.lower().strip() == 'a':
#         #     contador_ordenes +=1
            # mover_adelante(direccion, x)