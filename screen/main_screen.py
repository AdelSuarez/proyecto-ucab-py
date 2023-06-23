import pygame

import style.style as st
from src.create_map import Create_map
from src.move import Move
from src.robot_rotation import Robot_rotation
from src.collision_checker import Collision_checker
from screen.create_map_screen import Create_map_screen
from components.Button import Button
from components.Text import Text
import assets.Assets as ast

class Main_screen:
    def __init__(self):
        pygame.init()
        self._font = pygame.font.SysFont("arialblack", 70)
        self._game_over = False
        self._game_pause = False
        self.address = 'E'
        self.map_game = Create_map(17,23).maker()

        # ------------------------ ASSETS -----------------------------------------------------
        # self._robot= pygame.transform.scale(pygame.image.load("screen/assets/robot.png"), (40, 40))
        # self._robot = pygame.transform.scale(pygame.image.load("assets/robot1.png"), (50, 50))
        # self._bomb = pygame.transform.scale(pygame.image.load("assets/bomba.png"), (35, 35))
        # self._goal = pygame.transform.scale(pygame.image.load("assets/unavainaloca.png"), (35, 35))
        # self._over = pygame.transform.scale(pygame.image.load("assets/explosion.png"), (45, 45))
        # self._victory = pygame.transform.scale(pygame.image.load("assets/victory.png"), (50, 50))
        # self._btn_start = pygame.image.load("assets/start_btn.png")
        # self._btn_exit = pygame.image.load("assets/exit_btn.png")
        # self._game_over_img =  pygame.transform.scale(pygame.image.load("assets/Background1.png"), (600,400)) 
        # self._victory_img =  pygame.transform.scale(pygame.image.load("assets/victory.png"), (700,500))
        # self.b = pygame.image.load("assets/b_opacity.png")



        self.settings()
        # self._screen_victory()
        self._menu()

    def settings(self):
        self._size = (1042, 772)

        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        self._clock = pygame.time.Clock()
        

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
            Create_map_screen(self.map_game, self._screen, ast.robot, self.address, ast.bomb, ast.goal, ast.victory, ast.over)

            if Collision_checker(self.map_game).checker() == '#':
                self._screen_game_over()
            elif  Collision_checker(self.map_game).checker() == '@':
                self._screen_victory()

            pygame.display.update()
            self._clock.tick(60)

    def _menu(self):
        while not self._game_over:
            self._screen.fill((52,78,91))

            if self._game_pause:
                #game
                self._game()
            else:
                # Menu
                Text('MENU PRINCIPAL', self._font, st.WHITE,).draw_text(self._screen, 200,50)
                if Button(300, 300, ast.btn_start, 1.5).draw(self._screen):
                    self._game_pause = True
                elif Button(390,600,ast.btn_exit,1).draw(self._screen):
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

    def _screen_game_over(self):
        while not self._game_over:
            self._screen.blit(ast.b, (0,0))

            self._screen.blit(ast.game_over_img, (220,180))


            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._game_pause = True
            pygame.display.update()
            self._clock.tick(60)


    def _screen_victory(self):
        while not self._game_over:
            self._screen.blit(ast.b, (0,0))
            self._screen.blit(ast.victory_img, (150,120))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._game_pause = True
            pygame.display.update()
            self._clock.tick(60)
