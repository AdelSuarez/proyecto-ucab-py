import pygame
import style.style as st
import assets.Assets as asset
from src.move import Move
from src.robot_rotation import Robot_rotation
from src.collision_checker import Collision_checker
from screen.create_map_screen import Create_map_screen
from screen.Screen_state import Screen_state
# import screen.Screen_menu as a

class Screen_game:
    def __init__(self, game_over, address, map_game, game_pause, clock) -> None:
        self.game_over = game_over
        self.address = address
        self.map_game = map_game
        self.game_pause = game_pause
        self.clock = clock
    


    def game(self, screen):
         while not self.game_over:

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    if key == 'a':
                        Move(self.address, self.map_game).advance()
                    elif key == 'd':
                        self.address = Robot_rotation(self.address, self.map_game).right()
                    elif key == 'i':
                        self.address = Robot_rotation(self.address, self.map_game).left()
                    

            screen.fill(st.BLACK)
            Create_map_screen(self.map_game, screen, asset.robot, self.address, asset.bomb, asset.goal, asset.victory, asset.over)

            if Collision_checker(self.map_game).checker() == '#':
                Screen_state(asset.b, asset.game_over_img, self.game_over, self.clock).game_over(screen)

            elif  Collision_checker(self.map_game).checker() == '@':
                Screen_state(asset.b, asset.victory_img, self.game_over, self.clock).victory(screen)

            pygame.display.update()
            self.clock.tick(60)