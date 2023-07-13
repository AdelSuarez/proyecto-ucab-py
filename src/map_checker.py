import random

class Map_checker:

    def __init__(self, column, map_game):
        self._column = column
        self.map_game = map_game

    def checker(self):
    # recorre el mapa para modificar error con la ubicacion de la meta y las minas, para evitar generar mapas imposibles de pasar
        list = random.randint(1,3)
        value = random.randint(1,(self._column-1))

        # ! Seguir mejorando el verificador del mapa
        for index_row, row in enumerate(self.map_game):
            for index_column, column in enumerate(row):
                
                if index_row == 0:
                    # verifica si el robot esta en la primera fila y en la primera columna, y si se encuentra rodeado de bombas, elimna la que tiene a la derecha
                    if index_column == 0 and column == '>':
                        if row[index_column+1] == '*' and self.map_game[index_row+1][index_column] == '*':
                            row[index_column+1] = ' '

                if (index_row == 0 or index_row == 1 or  index_row == 2) and column == 'H':
                    # Condicional que verifica si la meta se encuentra en las primeras tres filas, si se encuentra la coloca en las ultimas filas del mapa
                    row[index_column] = ' '
                    try:
                        self.map_game[-list][value] = 'H'
                    except Exception:
                        self.map_game[-list][-1] = 'H'
                            
                
                if column == '>':
                    # verifica si hay dos bombas al lado del robot de derecha e izquierda, elimina la de la parte de la derecha
                    try:
                        if row[index_column+1] == '*' and row[index_column-1] == '*':
                            row[index_column+1] = ' '
                    except Exception:
                        pass

                if column == 'H':
                    # verifica si hay dos bombas al lado de la meta de derecha e izquierda, elimina la de la parte de la derecha
                    try:
                        if row[index_column+1] == '*' and row[index_column-1] == '*':
                            row[index_column+1] = ' '
                    except Exception:
                        pass

                if column == '*':
                    
                    try:
                        # Elimina una mina si se encuentran dos seguidas
                        if row[index_column+1] == '*':
                            row[index_column+1] = ' '
                    except Exception:
                        pass

                    if index_row%2 == 1:
                        try:
                            # Elimina minas que se encuentran seguidas de forma vertical
                            if self.map_game[index_row+1][index_column] == '*':
                                self.map_game[index_row+1][index_column] = ' '
                        except Exception:
                            pass

                        try:
                            # Elimina minas si se encuentran dos diagonales (direccion derecha)
                            if self.map_game[index_row+1][index_column+1] == '*':
                                self.map_game[index_row+1][index_column+1] = ' '
                        except Exception:
                            pass

                    if index_row%2 == 0 or index_row%2 == 1:
                        try:
                            # Elimina minas si se encuentran dos diagonales (direccion izquierda)

                            if self.map_game[index_row+1][index_column-1] == '*':
                                self.map_game[index_row+1][index_column-1] = ' '
                        except Exception:
                            pass