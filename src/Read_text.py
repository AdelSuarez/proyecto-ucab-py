class Read_text:
    def __init__(self) -> None:
        count = 1
        self.map_game = []
        self.open = open('mapa.txt', 'r', encoding='UTF-8')

        self.size_map = [int(i) for i in self.open.readline().split(',')]

        print(self.size_map)

        for i in range(self.size_map[0]):
            for j in self.open.readlines(i+1): 
                row = [int(i) for i in j.split(',')]
            self.map_game.append(row)
            count += 1

        # position robot
        self.robot = [int(i) for i in self.open.readline(count+1).split(',')]

        # position goal        
        self.goal = [int(i) for i in self.open.readline(count+2).split(',')]

        self.address = self.open.readline(count+3)
        print(self.open.readline(count+4))

        self.moves = [i for i in self.open.readline(count+5).split(' ')]


    def convert_map(self):
        for index_row, row in enumerate(self.map_game):
            for index_colum,column in enumerate(row):
                if column == 1:
                    self.map_game[index_row][index_colum] = '*'
                if column == 0:
                    self.map_game[index_row][index_colum] = ' '

        self.selection_address()
        self.map_game[self.goal[0]-1][self.goal[1]-1] = 'H'

        return (self.map_game, self.moves)
    
    def selection_address(self):
        self.address.upper().strip()
        if self.address == 'E\n':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = '>'
        elif self.address == 'S\n':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = 'v'
        elif self.address == 'O\n':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = '<'
        elif self.address == 'N\n':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = '^'
                      





