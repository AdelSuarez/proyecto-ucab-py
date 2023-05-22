

class Archivo:
    def __init__(self, row, column, map_game) -> None:
        self._row = row
        self._column = column
        self._map_game = map_game

    def save(self): 
        self._arch = open('robotcok.txt', 'w')
        self._arch.write(f'{self._column},{self._row}\n')
        self.a()
        self._arch.close()

    def a(self):
        for i in range(len(self._map_game)):
            count = 1
            for j in self._map_game[i]:
                if count < self._column:
                    if j == ' ':
                        self._arch.write('0,')
                        count+=1
                    elif j == '*':
                        self._arch.write('1,')
                        count+=1
                    else:
                        self._arch.write(f'{j},')
                        count+=1
                elif count == self._column:
                    if j == ' ':
                        self._arch.write('0\n')
                    elif j == '*':
                        self._arch.write('1\n')
                    else:
                        self._arch.write(f'{j}\n')



