class Read_text:
    def __init__(self) -> None:
        self.map_game = []
        self.open = open('mapa.txt', 'r', encoding='UTF-8')

        self.size_map = [int(i) for i in self.open.readline().split(',')]

        print(self.size_map)

        for i in range(self.size_map[0]):
            for j in self.open.readlines(i+1): 
                row = [int(i) for i in j.split(',')]
            self.map_game.append(row)

        

        for i in self.map_game:
            print(i)

        # position robot
        self.robot = [int(i) for i in self.open.readline(self.size_map[0]+2).split(',')]

        print(self.robot)

        # position goal        
        self.goal = [int(i) for i in self.open.readline(self.size_map[0]+3).split(',')]

        print(self.goal)



