import pygame

# import style.style as st
from src.create_map import Create_map
# from src.move import Move
# from src.robot_rotation import Robot_rotation
# from src.collision_checker import Collision_checker
# from screen.create_map_screen import Create_map_screen
# from components.Button import Button
# from components.Text import Text
# from screen.Screen_state import Screen_state
# from screen.Screen_game import Screen_game
from screen.Screen_menu import Screen_menu
# import assets.Assets as asset



class Main_screen:
    def __init__(self):
        pygame.init()
        self.game_over = False
        self.game_pause = False
        self.address = 'E'
        self.map_game = Create_map(17,23).maker()

        self.settings()
        Screen_menu(self.game_over, self.game_pause, self.address, self.map_game, self.clock).menu(self.screen)
        # self._screen_victory()
        # self._menu()

    def settings(self):
        self._size = (1042, 772)

        self.screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        self.clock = pygame.time.Clock()
        

    # def _game(self):
    #      while not self.game_over:

            
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 self.game_over = True
    #             if event.type == pygame.KEYDOWN:
    #                 key = pygame.key.name(event.key)
    #                 if key == 'a':
    #                     Move(self.address, self.map_game).advance()
    #                 elif key == 'd':
    #                     self.address = Robot_rotation(self.address, self.map_game).right()
    #                 elif key == 'i':
    #                     self.address = Robot_rotation(self.address, self.map_game).left()
    #                 elif event.key == pygame.K_SPACE:
    #                     self.game_pause= False
    #                     self._menu()

    #         self._screen.fill(st.BLACK)
    #         Create_map_screen(self.map_game, self._screen, asset.robot, self.address, asset.bomb, asset.goal, asset.victory, asset.over)

    #         if Collision_checker(self.map_game).checker() == '#':
    #             Screen_state(asset.b, asset.game_over_img, self.game_over, self._clock).game_over(self._screen)

    #         elif  Collision_checker(self.map_game).checker() == '@':
    #             Screen_state(asset.b, asset.victory_img, self.game_over, self._clock).victory(self._screen)

    #         pygame.display.update()
    #         self._clock.tick(60)

    # def _menu(self):
    #     while not self.game_over:
    #         self.screen.fill((52,78,91))

    #         if self.game_pause:
    #             #game
    #             Screen_game(self.game_over, self.address, self.map_game, self.game_pause, self.clock).game(self.screen)
    #         else:
    #             # Menu
    #             Text('MENU PRINCIPAL', self._font, st.WHITE,).draw_text(self.screen, 200,50)
    #             if Button(300, 300, asset.btn_start, 1.5).draw(self.screen):
            #         self.game_pause = True
            #     elif Button(390,600,asset.btn_exit,1).draw(self.screen):
            #         pygame.quit()
            #         self.game_over = True

            
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         self.game_over = True
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_SPACE:
            #             self.game_pause = True
                    
            # pygame.display.update()
            # self.clock.tick(60)

    # def _screen_game_over(self):
    #     while not self._game_over:
    #         self._screen.blit(asset.b, (0,0))

    #         self._screen.blit(asset.game_over_img, (220,180))


            
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 self._game_over = True
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     self._game_pause = True
    #         pygame.display.update()
    #         self._clock.tick(60)


    # def _screen_victory(self):
    #     while not self._game_over:
    #         self._screen.blit(asset.b, (0,0))
    #         self._screen.blit(asset.victory_img, (150,120))

    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 self._game_over = True
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_SPACE:
    #                     self._game_pause = True
    #         pygame.display.update()
    #         self._clock.tick(60)
