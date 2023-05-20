class Collision_checher:
    def __init__(self, map_game):
        self.map_game =map_game


    def checker(self):
        for fila in self.map_game:
            for columna in fila:
                if columna == '#':
                    return '#'
                elif columna == '@':
                    return '@'