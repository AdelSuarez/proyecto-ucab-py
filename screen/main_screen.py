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
        self.wiget_main()

    def settings(self):
        self._game_over = False
        self._size = (1042, 772)
        pygame.init()
        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        self._clock = pygame.time.Clock()

    def wiget_main(self):

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
                pygame.draw.rect(self._screen,
                                st.GREY,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                
                try:
                    if self.map_game[row][index_column+1] == '<' and column == ' ' and self.address == 'O':

                        pygame.draw.rect(self._screen,
                                st.GREEN_ROBOT,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG]) 
                        
                    elif self.map_game[row][index_column+1] == '<' and column == '*' and self.address == 'O':
                        pygame.draw.rect(self._screen,
                                st.RED_SCREEN,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG]) 
                except Exception:
                    pass

                try:
                    if self.map_game[row+1][index_column] == '^' and column == ' ' and self.address == 'N':

                        pygame.draw.rect(self._screen,
                                st.GREEN_ROBOT,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                    elif self.map_game[row+1][index_column] == '^' and column == '*' and self.address == 'N':
                        pygame.draw.rect(self._screen,
                                st.RED_SCREEN,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG]) 
                except Exception:
                    pass
                if self.map_game[row][index_column-1] == '>' and column == ' ' and self.address == 'E':
                    pygame.draw.rect(self._screen,
                                st.GREEN_ROBOT,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                elif self.map_game[row][index_column-1] == '>' and column == '*' and self.address == 'E':
                    pygame.draw.rect(self._screen,
                                st.RED_SCREEN,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                    
                if self.map_game[row-1][index_column] == 'v' and column == ' ' and self.address == 'S':
                    pygame.draw.rect(self._screen,
                                st.GREEN_ROBOT,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                elif self.map_game[row-1][index_column] == 'v' and column == '*' and self.address == 'S':
                    pygame.draw.rect(self._screen,
                                st.RED_SCREEN,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                    







                if column == '>' or column == '<' or column == 'v' or column == '^':   
                    pygame.draw.rect(self._screen,
                                st.GREEN_ROBOT,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])
                    self._screen.blit(self._robot, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN-5,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-8,
                                st.HIGH,
                                st.LONG])
# -----------------------------------------------------------------------------------------------------
                
                   
                
                      
                # elif self.map_game[row+1][index_column] == '^' and column == ' ':

                #     pygame.draw.rect(self._screen,
                #                 st.GREEN_SCREEN,
                #                 [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                #                 (st.MARGIN+st.LONG) * row + st.MARGIN,
                #                 st.HIGH,
                                # st.LONG]) 
# -----------------------------------------------------------------------------------------------------
                    

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
                    self._screen.blit(self._victory, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN-7,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-5,
                                st.HIGH,
                                st.LONG])

                