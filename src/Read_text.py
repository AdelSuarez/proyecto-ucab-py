class Read_text:
    def __init__(self) -> None:
        count = 1
        self.map_game = []
        with open('mapa.txt', 'r', encoding='UTF-8') as self.open:

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


            self.moves = self.open.readlines(count+5)
            # self.more_moves = [i for i in self.open.readline(count+6).split(' ')]
            # print(self.more_moves)


    def convert_map(self):
        for index_row, row in enumerate(self.map_game):
            for index_colum,column in enumerate(row):
                if column == 1:
                    self.map_game[index_row][index_colum] = '*'
                if column == 0:
                    self.map_game[index_row][index_colum] = ' '

        self.selection_address()
        self.map_game[self.goal[0]-1][self.goal[1]-1] = 'H'
        return (self.map_game, self.all_moves())
    
    def all_moves(self):
        return [i for i in self.moves[0].split(' ')]
        

    
    def selection_address(self):
        if self.address.strip('\n').upper() == 'E':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = '>'
        elif self.address.strip('\n').upper() == 'S':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = 'v'
        elif self.address.strip('\n').upper() == 'O':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = '<'
        elif self.address.strip('\n').upper() == 'N':
            self.map_game[self.robot[0]-1][self.robot[1]-1] = '^'
                      





if __name__ == '__main__':
    print('hola')
    Read_text().all_moves()