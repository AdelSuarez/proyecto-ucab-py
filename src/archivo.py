class Archivo:
    def __init__(self, row, column, map_game, position_robot_row, position_robot_column, position_goal_row, position_goal_column, address, counter, movement, event) -> None:
        self._row = row
        self._column = column
        self._map_game = map_game
        self._r_row = position_robot_row
        self._r_column = position_robot_column
        self._g_row = position_goal_row
        self._g_column = position_goal_column
        self._address = address
        self._counter = counter
        self._movement = movement
        self._event = event
        self.save()
        
    def save(self): 
        self._arch = open('robotcok.txt', 'w')
        self._arch.write(f'{self._column},{self._row}\n')
        self._map_converter()
        self._arch.write(f'{self._r_column},{self._r_row}\n')
        self._arch.write(f'{self._g_column},{self._g_row}\n')
        self._arch.write(f'{self._address}\n')
        self._arch.write(f'{self._counter}\n')
        self._arch.write(f'{self._movement}\n')
        if self._event == '#' or self._counter >40:
            self._arch.write('N\n')
        elif self._event == '@':
            self._arch.write('Y\n')

        self._arch.close()

    def _map_converter(self):
        for row in range(len(self._map_game)):
            for index_column,column in enumerate(self._map_game[row]):
                if index_column == len(self._map_game[row])-1:
                    if column == ' ':
                        self._arch.write('0\n')
                    elif column == '*':
                        self._arch.write('1\n')
                    else:
                        self._arch.write(f'{column}\n')
                else:
                    if column == ' ':
                        self._arch.write('0,')
                    elif column == '*':
                        self._arch.write('1,')
                    else:
                        self._arch.write(f'{column},')



