import pygame
# from src.create_map import Create_map
from src.create_map import Create_map
import style.style as st
from cmd.move import Move
from cmd.robot_rotation import Robot_rotation

class Main_screen:
    def __init__(self):
        self.address = 'E'
        self.map_game = Create_map(17,23).maker()
        # self._robot= pygame.transform.scale(pygame.image.load("screen/assets/robot.png"), (40, 40))
        self._robot= pygame.transform.scale(pygame.image.load("screen/assets/robot1.png"), (50, 50))

        self._bomb= pygame.transform.scale(pygame.image.load("screen/assets/bomba.png"), (35, 35))
        self._goal= pygame.transform.scale(pygame.image.load("screen/assets/meta.png"), (35, 35))
        self._over= pygame.transform.scale(pygame.image.load("screen/assets/explosion.png"), (45, 45))
        self._victory= pygame.transform.scale(pygame.image.load("screen/assets/victory.png"), (50, 50))

        self.settings()
        self.widget_main()

    def settings(self):
        self._game_over = False
        self._size = (1042, 772)
        pygame.init()
        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        self._clock = pygame.time.Clock()

    def widget_main(self):

        while not self._game_over:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    tecla = pygame.key.name(event.key)
                    if tecla == 'a':
                        Move(self.address, self.map_game).advance()
                    if tecla == 'd':
                        self.address = Robot_rotation(self.address, self.map_game).right()
                    if tecla == 'i':
                        self.address = Robot_rotation(self.address, self.map_game).left()

            self._screen.fill(st.BLACK)
            self.create_map()


            self._clock.tick(60)
            pygame.display.update()


    def create_map(self):
        for row in range(len(self.map_game)):
            for index_column, column in enumerate(self.map_game[row]):
                self._color_position(st.GREY, index_column, row)

                self._sensor_left( row, index_column, column)
                
                self._sensor_top( row, index_column, column)

                self._sensor_right( row, index_column, column)

                self._sensor_lower( row, index_column, column)

                if column == '>' or column == '<' or column == 'v' or column == '^':
                    self._color_robot_top( row, column, index_column)

                    self._color_robot_left( row, column, index_column)

                    self._color_robot_right( row, column, index_column)

                    self._color_robot_lower( row, column, index_column)
                                            
                    self._screen.blit(self._robot, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN-5,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-8,
                                st.HIGH,
                                st.LONG])
                    

                elif column == '*':
                    
                    self._screen.blit(self._bomb, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN+2,
                                (st.MARGIN+st.LONG) * row + st.MARGIN+5,
                                st.HIGH,
                                st.LONG])
                


                elif column == 'H':
                    self._screen.blit(self._goal, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN+2,
                                (st.MARGIN+st.LONG) * row + st.MARGIN+2,
                                st.HIGH,
                                st.LONG])
                    
                elif column == '#':
                    self._screen.blit(self._over, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-3,
                                st.HIGH,
                                st.LONG])
                    
                elif column == '@':
                    self._color_position(st.GOAL, index_column, row)
                    self._screen.blit(self._victory, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN-7,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-5,
                                st.HIGH,
                                st.LONG])

    def _color_position(self, color, index_column, row):
        pygame.draw.rect(self._screen,
                                color,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])


    def _collesion(self, robot, index_column, row, fila):
        for j in self.map_game[fila]:
            if j == robot:
                pygame.draw.rect(self._screen,
                    st.GREY,
                    [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                    (st.MARGIN+st.LONG) * row + st.MARGIN,
                    st.HIGH,
                    st.LONG])
                break

    def _error_collesion_right(self, row, index_column):
        for j in self.map_game[row][-1]:
            if j =='>':
                self._color_position(st.WHITE, index_column, row)
                break

    def _sensor_left(self, row, index_column, column):
        try:
            if self.map_game[row][index_column+1] == '<' and column == ' ' and self.address == 'O':
                self._color_position(st.GREEN_ROBOT, index_column, row)

            elif self.map_game[row][index_column+1] == '<' and column == '*' and self.address == 'O':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif self.map_game[row][index_column+1] == '<' and column == 'H' and self.address == 'O':
                self._color_position(st.GOAL, index_column, row)

        except Exception:
            pass
    
    def _sensor_right(self, row, index_column, column):
        if self.map_game[row][index_column-1] == '>' and column == ' ' and self.address == 'E':
            self._color_position(st.GREEN_ROBOT, index_column, row)
            self._error_collesion_right(row, index_column)
            
        elif self.map_game[row][index_column-1] == '>' and column == '*' and self.address == 'E':
            self._color_position(st.RED_SCREEN, index_column, row)
            self._error_collesion_right(row, index_column)

        elif self.map_game[row][index_column-1] == '>' and column == 'H' and self.address == 'E':
            self._color_position(st.GOAL, index_column, row)

    def _sensor_top(self, row, index_column, column):
        try:
            if self.map_game[row+1][index_column] == '^' and column == ' ' and self.address == 'N':
                self._color_position(st.GREEN_ROBOT, index_column, row)

            elif self.map_game[row+1][index_column] == '^' and column == '*' and self.address == 'N':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif self.map_game[row+1][index_column] == '^' and column == 'H' and self.address == 'N':
                self._color_position(st.GOAL, index_column, row)
                
        except Exception:
            pass

    def _sensor_lower(self, row, index_column, column):
        if self.map_game[row-1][index_column] == 'v' and column == ' ' and self.address == 'S':
            self._color_position(st.GREEN_ROBOT, index_column, row)
            self._collesion('v', index_column, row, -1)

        elif self.map_game[row-1][index_column] == 'v' and column == '*' and self.address == 'S':
            self._color_position(st.RED_SCREEN, index_column, row)
            self._collesion('v', index_column, row, -1)
            
        elif self.map_game[row-1][index_column] == 'v' and column == 'H' and self.address == 'S':
            self._color_position(st.GOAL, index_column, row)

    def _color_robot_top(self, row, column, index_column):
        if column == '^' and (self.map_game[row-1][index_column] == '*' or row == 0):
            self._color_position(st.RED_SCREEN, index_column, row)

        elif column == '^' and self.map_game[row-1][index_column] == 'H':
            self._color_position(st.GOAL, index_column, row)
            
        else:
            self._color_position(st.GREEN_ROBOT, index_column, row)

    def _color_robot_left(self, row, column, index_column):
        if index_column-1 == -1 and self.address == 'O':
            self._color_position(st.RED_SCREEN, index_column, row)

        elif column == '<' and self.map_game[row][index_column-1] == '*' :
            self._color_position(st.RED_SCREEN, index_column, row)

        elif column == '<' and self.map_game[row][index_column-1] == 'H' :
            self._color_position(st.GOAL, index_column, row)

    def _color_robot_right(self, row, column, index_column):
        try:
            if column == '>' and self.map_game[row][index_column+1] == '*':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif column == '>' and self.map_game[row][index_column+1] == 'H':
                self._color_position(st.GOAL, index_column, row)
                
        except  IndexError:
            self._color_position(st.RED_SCREEN, index_column, row)


    def _color_robot_lower(self, row, column, index_column):
        try:
            if column == 'v' and self.map_game[row+1][index_column] == '*':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif column == 'v' and self.map_game[row+1][index_column] == 'H':
                self._color_position(st.GOAL, index_column, row)

        except  IndexError:
            self._color_position(st.RED_SCREEN, index_column, row)  
