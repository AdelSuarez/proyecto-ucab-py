class Robot_direction:
    movement_made = False

    def __init__(self, address, map_game):
        self.address = address
        self.map_game = map_game
        self.direction()

    def direction(self):
        Robot_direction.movement_made = False
        for row in self.map_game:
            for index_column, column in enumerate(row):
                if self.address == 'E':
                    if column == '>' or column == '^' or column == '<' or column == 'v':
                        self.check_direction_robot(
                            column, row, index_column, '>')
                        break

                elif self.address == 'S':
                    if column == '>' or column == '^' or column == '<' or column == 'v':
                        self.check_direction_robot(
                            column, row, index_column, 'v')
                        break

                elif self.address == 'O':
                    if column == '>' or column == '^' or column == '<' or column == 'v':
                        self.check_direction_robot(
                            column, row, index_column, '<')
                        break

                elif self.address == 'N':
                    if column == '>' or column == '^' or column == '<' or column == 'v':
                        self.check_direction_robot(
                            column, row, index_column, '^')
                        break

            if Robot_direction.movement_made:
                break

        return self.address

    def address_robot(self, row, index_column, robot):
        row[index_column] = robot
        Robot_direction.movement_made = True

    def check_direction_robot(self, column, row, index_column, robot):
        if column == '>' or column == '^' or column == '<' or column == 'v':
            self.address_robot(row, index_column, robot)
