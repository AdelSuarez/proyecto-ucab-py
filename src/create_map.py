import random
from . import map_checker

class CreateMap():
    robot = True
    goal = True
    assets= [' ', '*', 'H', '>']

    def __init__(self, row, column):
        self.__row = row
        self.__column = column
        self.map_game = []


    def maker(self):
        # Crear el tamaño del mapa segun los parametros introducidos
        for row in range(self.__row):
            # Ciclo que crea las filas
            self.map_game.append([])
            for column in range(self.__column):
                while True:
                    # Selecciona un assest al hazar de la lista para crear mapas aleatorios
                    asset = random.choice(CreateMap.assets)
                    if asset != '>' and asset != 'H':
                        break
                    elif CreateMap.robot :
                        if asset == '>':
                            CreateMap.robot = False
                            break
                    elif CreateMap.goal:
                        if asset == 'H':
                            CreateMap.goal = False
                            break

                    
                self.map_game[row].append(asset)

        map_checker.MapChecker(self.__column, self.map_game).checker()

        CreateMap.robot = True
        CreateMap.goal = True

        return self.map_game
                