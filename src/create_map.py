import random
from src.map_checker import Map_checker

class Create_map():
    robot = True
    goal = True
    assets= [' ', '*', 'H', '>']

    def __init__(self, row, column):
        self._row = row
        self._column = column
        self.map_game = []



    def maker(self):
        # Crear el tamaño del mapa segun los parametros introducidos
        for row in range(self._row):
            # Ciclo que crea las filas
            self.map_game.append([])
            for column in range(self._column):
                while True:
                    # Selecciona un assest al hazar de la lista para crear mapas aleatorios
                    asset = random.choice(Create_map.assets)
                    if asset != '>' and asset != 'H':
                        break
                    elif Create_map.robot :
                        if asset == '>':
                            Create_map.robot = False
                            break
                    elif Create_map.goal:
                        if asset == 'H':
                            Create_map.goal = False
                            break

                    
                self.map_game[row].append(asset)

        Map_checker(self._column, self.map_game).checker()
        return self.map_game
                