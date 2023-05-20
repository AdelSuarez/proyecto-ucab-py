import random

class Map_checker:

    def __init__(self, column, map_game):
        self._column = column
        self.map_game = map_game

    def checker(self):
    # recorre el mapa para modificar error con la la ubicacion de la meta y las monas, para evitar gener mapas imposibles de pasar
        a = random.randint(1,3)
        b = random.randint(1,(self._column-1))

        # TODO verificar cuando el mapa es pequeño, por ejempo 9x3 que se crean bloqueos, de igual formar, verificar la meta que no se bloquee con minas
        # ! Seguir mejorando el verificador del mapa
        for index_fila, fila in enumerate(self.map_game):
            for index_columna, columna in enumerate(fila):
                
                if index_fila == 0:
                    # verifica si el robot esta en la primera fila y en la primera columna, y si se encuentra rodeado de bombas, elimna la que tiene a la derecha
                    if index_columna == 0 and columna == '>':
                        if fila[index_columna+1] == '*' and self.map_game[index_fila+1][index_columna] == '*':
                            fila[index_columna+1] = ' '

                if (index_fila == 0 or index_fila == 1 or  index_fila == 2) and columna == 'H':
                    # Condicional que verifica si la meta se encuantra en las primeras tres filas, si se encuentra la coloca en las ultimas filas del mapa
                    fila[index_columna] = ' '
                    try:
                        self.map_game[-a][b] = 'H'
                    except Exception:
                        self.map_game[-a][-1] = 'H'
                            
                
                if columna == '>':
                    # verifica si hay dos bombas al lado del robot de derecha e izquierda, elimina la de la parte de la derecha
                    try:
                        if fila[index_columna+1] == '*' and fila[index_columna-1] == '*':
                            fila[index_columna+1] = ' '
                    except Exception:
                        pass

                if columna == 'H':
                    # verifica si hay dos bombas al lado del robot de derecha e izquierda, eliminpassa la de la parte de la derecha
                    try:
                        if fila[index_columna+1] == '*' and fila[index_columna-1] == '*':
                            fila[index_columna+1] = ' '
                    except Exception:
                        pass

                if columna == '*':
                    
                    try:
                        # Elimana mina si se encuentras dos seguidas
                        if fila[index_columna+1] == '*':
                            fila[index_columna+1] = ' '
                    except Exception:
                        pass

                    if index_fila%2 == 1:
                        try:
                            # elimina minas que se encuentra seguidas de forma vertical
                            if self.map_game[index_fila+1][index_columna] == '*':
                                self.map_game[index_fila+1][index_columna] = ' '
                        except Exception:
                            pass

                        try:
                            # elimina minas si se encuentran dos diagonales direccion derecha
                            if self.map_game[index_fila+1][index_columna+1] == '*':
                                self.map_game[index_fila+1][index_columna+1] = ' '
                        except Exception:
                            pass

                    if index_fila%2 == 0 or index_fila%2 == 1:
                        try:
                            # elimina minas si se encuentran dos diagonales direccion izquierda

                            if self.map_game[index_fila+1][index_columna-1] == '*':
                                self.map_game[index_fila+1][index_columna-1] = ' '
                        except Exception:
                            pass