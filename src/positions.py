class Positions:

    def __init__(self, map_game):
        self.map_game = map_game

    def position_robot(self):
        # * Muestra la ubicacion del robot en tiempo real 
        position_row_robot = 0
        position_column_robot = 0
        robot = ''
        is_position  = False

        for  index_row ,row in enumerate(self.map_game):
            for index_column , value in enumerate(row):
                if value == '>' or value == '<' or value == 'v' or value == '^' or value == '#':
                    position_row_robot = index_row+1
                    position_column_robot = index_column+1

                    if value == '#':
                        robot = 'X'

                    else:
                        robot = value

                    is_position = True
                    break   
                           
            if is_position:
                break

        return (position_row_robot, position_column_robot, robot)

    def position_goal(self):
        # se busca la ubicacion de la meta de forma independiente debido a que esta funcion solo se va llamar una vez
        position_row_goal = 0
        position_column_goal = 0
        is_position  = False

        for  index_row ,row in enumerate(self.map_game):
            for index_column , value in enumerate(row):
                if value == 'H':
                    position_row_goal = index_row+1
                    position_column_goal = index_column+1
                    is_position = True
                    break                    
            if is_position:
                break

        return ( position_row_goal, position_column_goal )