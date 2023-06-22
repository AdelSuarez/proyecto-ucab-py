import pygame
# from src.create_map import Create_map
from src.create_map import Create_map
import style.style as st
from src.move import Move
from src.robot_rotation import Robot_rotation
from screen.create_map_screen import Create_map_screen
from components.Button import Button

class Main_screen:
    def __init__(self):
        pygame.init()
        self._font = pygame.font.SysFont("arialblack", 80)
        self._game_over = False
        self._game_pause = False
        self.address = 'E'
        self.map_game = Create_map(17,23).maker()

        # ------------------------ ASSETS ----------------------------------------------------------- 
        # self._robot= pygame.transform.scale(pygame.image.load("screen/assets/robot.png"), (40, 40))
        self._robot = pygame.transform.scale(pygame.image.load("screen/assets/robot1.png"), (50, 50))
        self._bomb = pygame.transform.scale(pygame.image.load("screen/assets/bomba.png"), (35, 35))
        self._goal = pygame.transform.scale(pygame.image.load("screen/assets/unavainaloca.png"), (35, 35))
        self._over = pygame.transform.scale(pygame.image.load("screen/assets/explosion.png"), (45, 45))
        self._victory = pygame.transform.scale(pygame.image.load("screen/assets/victory.png"), (50, 50))
        self._btn_start = pygame.image.load("screen/assets/start_btn.png")
        self._btn_exit = pygame.image.load("screen/assets/exit_btn.png")


        self.settings()
        self._menu()
        # self.widget_main()

    def settings(self):
        self._size = (1042, 772)

        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        self._clock = pygame.time.Clock()
        

    def draw_text(self,text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self._screen.blit(img, (x,y))

    # def widget_main(self):
    #     while not self._game_over:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 self._game_over = True
    #             if event.type == pygame.KEYDOWN:
    #                 key = pygame.key.name(event.key)
    #                 if key == 'q':
    #                     self._game()

                

    #         self._menu()


    def _game(self):
         while not self._game_over:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    if key == 'a':
                        Move(self.address, self.map_game).advance()
                    elif key == 'd':
                        self.address = Robot_rotation(self.address, self.map_game).right()
                    elif key == 'i':
                        self.address = Robot_rotation(self.address, self.map_game).left()
                    elif event.key == pygame.K_SPACE:
                        self._game_pause= False
                        self._menu()

            self._screen.fill(st.BLACK)
            Create_map_screen(self.map_game, self._screen, self._robot, self.address, self._bomb, self._goal, self._victory, self._over)


            pygame.display.update()
            self._clock.tick(60)

    def _menu(self):
        while not self._game_over:
            self._screen.fill((52,78,91))

            if self._game_pause:
                #game
                self._game()
                # screen menu
            else:
                # Menu
                self.draw_text('MENU PRINCIPAL', self._font, st.WHITE, 280,50)
                if Button(300,300,self._btn_start,1.5).draw(self._screen):
                    self._game_pause = True
                elif Button(390,600,self._btn_exit,1).draw(self._screen):
                    pygame.quit()
                    self._game_over = True

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._game_pause = True
                    
                        
                        
                


            pygame.display.update()
            self._clock.tick(60)

