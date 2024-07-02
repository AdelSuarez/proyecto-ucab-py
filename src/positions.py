class Positions:

    def __init__(self, map_game):
        self.map_game = map_game

    def position_robot(self) -> tuple[int, int, str]:
        # * Muestra la ubicacion del robot en tiempo real
        position_row_r: int = 0
        position_column_r: int = 0
        robot: str = ''

        is_position = False
        for index_row, row in enumerate(self.map_game):
            for index_column, value in enumerate(row):
                if value == '>' or value == '<' or value == 'v' or value == '^' or value == '#':
                    position_row_r = index_row+1
                    position_column_r = index_column+1

                    if value == '#':
                        robot = 'X'
                    else:
                        robot = value

                    is_position = True
                    break
            if is_position:
                break

        return (position_row_r, position_column_r, robot)

    def position_goal(self) -> tuple[int, int]:
        # se busca la ubicacion de la meta de forma independiente debido a que esta funcion solo se va llamar una vez
        position_row_m: int = 0
        position_column_m: int = 0
        is_position: bool = False

        for index_row, row in enumerate(self.map_game):
            for index_column, value in enumerate(row):
                if value == 'H':
                    position_row_m = index_row+1
                    position_column_m = index_column+1
                    is_position = True
                    break
            if is_position:
                break

        return (position_row_m, position_column_m)
