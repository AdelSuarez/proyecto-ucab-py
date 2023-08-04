class RobotRotation:
    movement_made = False

    def __init__(self, address, map_game):
        self.address = address
        self.map_game = map_game

    def left(self):
        RobotRotation.movement_made = False
        for row in self.map_game:
            for index_column, column in enumerate(row):
                if column == '>':
                    self.address_robot(row, index_column, 'N', '^')
                    break

                elif column == '^':
                    self.address_robot(row, index_column, 'O', '<')
                    break

                elif column == '<':
                    self.address_robot(row, index_column, 'S', 'v')
                    break

                elif column == 'v':
                    self.address_robot(row, index_column, 'E', '>')
                    break

            if RobotRotation.movement_made:
                break
            
        return self.address



    def right(self):
        # Cambia la direccion del robot, solo direccion derecha
        RobotRotation.movement_made = False
        for row in self.map_game:
            for index_column, column in enumerate(row):
                if column == '>':
                    self.address_robot(row, index_column, 'S', 'v')
                    break

                elif column == 'v':
                    self.address_robot(row, index_column, 'O', '<')
                    break

                elif column == '<':
                    self.address_robot(row, index_column, 'N', '^')
                    break

                elif column == '^':
                    self.address_robot(row, index_column, 'E', '>')
                    break
                
            if RobotRotation.movement_made:
                break

        return self.address


    def address_robot(self,row, index_column, address, robot):
        self.address = address
        row[index_column] = robot
        RobotRotation.movement_made = True