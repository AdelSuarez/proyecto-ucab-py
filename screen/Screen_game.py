import pygame
import style.style as st
import assets.Assets as asset
from src.move import Move
from src.robot_rotation import Robot_rotation
from src.collision_checker import Collision_checker
from src.positions import Positions
from screen.create_map_screen import Create_map_screen
from screen.Screen_state import Screen_state
from components.Text import Text

class Screen_game:
    counter_move = 0
    def __init__(self, game_over, address, map_game, game_pause) -> None:
        self._font = st.font(15)
        self.game_over = game_over
        self.address = address
        self.map_game = map_game
        self.game_pause = game_pause
        (self._position_row_goal, self._position_column_goal) = Positions(self.map_game).position_goal()

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
                        Screen_game.counter_move += 1
                    elif key == 'd':
                        self.address = Robot_rotation(self.address, self.map_game).right()
                        Screen_game.counter_move += 1

                    elif key == 'i':
                        self.address = Robot_rotation(self.address, self.map_game).left()
                        Screen_game.counter_move += 1


            screen.fill(st.BLACK)
            Create_map_screen(self.map_game, screen, asset.robot, self.address, asset.bomb, asset.goal, asset.victory, asset.over)

            if Collision_checker(self.map_game).checker() == '#' or Screen_game.counter_move == 41:
                Screen_state(asset.BG_opacity, self.game_over).game_over(screen,Collision_checker(self.map_game).checker())

            elif  Collision_checker(self.map_game).checker() == '@':
                Screen_state(asset.BG_opacity, self.game_over, asset.victory_img).victory(screen, Screen_game.counter_move)
            
            self.bar_state(screen)

            pygame.display.update()

    def bar_state(self,screen):
        # ----------------------Movements----------------------------------
        (self._position_row_robot, self._position_column_robot, self._robot) = Positions(self.map_game).position_robot()
        Text('Movements: ', self._font, st.WHITE).draw_text(screen, 60,780)
        Text(f'{Screen_game.counter_move} ', self._font, st.GREEN_ROBOT).draw_text(screen, 215,780)

        # ----------------------Address----------------------------------
        Text('Address: ', self._font, st.WHITE).draw_text(screen, 300,780)
        Text(f'{self.address} ', self._font, st.GREEN_ROBOT).draw_text(screen, 427,780)

        # ----------------------Robot----------------------------------
        Text('Robot:', self._font, st.WHITE).draw_text(screen, 520,780)
        Text(f'{self._position_row_robot} | {self._position_column_robot}', self._font, st.GREEN_ROBOT).draw_text(screen, 610,780)

        # ----------------------Goal----------------------------------
        Text('Goal:', self._font, st.WHITE).draw_text(screen, 750,780)
        Text(f'{self._position_row_goal} | {self._position_column_goal}', self._font, st.GREEN_ROBOT).draw_text(screen, 825,780)

        # ----------------------Origin Robot----------------------------------
        Text(f'{self._robot}', self._font, st.RED_ROBOT).draw_text(screen, 1000,780)
        
