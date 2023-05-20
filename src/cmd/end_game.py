import style.style as st
from src.cmd.clear_terminal import clear
from src.cmd.view_map import View_map

class End_game:
    def __init__(self, count, checker, column, map_game):
        self.count = count
        self.checker = checker
        self.column = column
        self.map_game = map_game
        self.end()

    def end(self):
        clear()
        View_map(self.column, self.map_game).view()
        print('')
        print('FIN DEL JUEGO'.center((self.column*4)+3, '-'))
        if self.count > 40:
            print(f'\n{st.GREEN}>>{st.RESET} Perdiste\n{st.GREEN}>>{st.RESET} Movientos agotados\n')
        elif self.checker == '#':
            print(f'\n{st.GREEN}>>{st.RESET} Perdiste\n{st.GREEN}>>{st.RESET} El robot a colisionado o tocado una mina\n')
        elif self.checker == '@':
            print(f'\n{st.GREEN}>>{st.RESET} Ganaste\n{st.GREEN}>>{st.RESET} Realizaste {self.count} movimientos para llegar a la meta\n')


