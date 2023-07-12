from src import positions
from components import Text
import style.style as st


class Status_bar():
    def __init__(self, map_game, counter_move, address) -> None:
        self._font_text_bar = st.font(15)
        self.map_game = map_game
        self.counter_move = counter_move
        self.address = address
        (self._position_row_goal, self._position_column_goal) = positions.Positions(self.map_game).position_goal()



    def bottom_status_bar(self, screen):
        # ----------------------Movements----------------------------------
        (self._position_row_robot, self._position_column_robot, self._robot) = positions.Positions(self.map_game).position_robot()
        Text.Text('Movements: ', self._font_text_bar, st.WHITE).draw_text(screen, 60,780)
        Text.Text(f'{self.counter_move} ', self._font_text_bar, st.GREEN_ROBOT).draw_text(screen, 215,780)

        # ----------------------Address----------------------------------
        Text.Text('Address: ', self._font_text_bar, st.WHITE).draw_text(screen, 300,780)
        Text.Text(f'{self.address} ', self._font_text_bar, st.GREEN_ROBOT).draw_text(screen, 427,780)

        # ----------------------Robot----------------------------------
        Text.Text('Robot:', self._font_text_bar, st.WHITE).draw_text(screen, 520,780)
        Text.Text(f'{self._position_row_robot} | {self._position_column_robot}', self._font_text_bar, st.GREEN_ROBOT).draw_text(screen, 610,780)

        # ----------------------Goal----------------------------------
        Text.Text('Goal:', self._font_text_bar, st.WHITE).draw_text(screen, 750,780)
        Text.Text(f'{self._position_row_goal} | {self._position_column_goal}', self._font_text_bar, st.GREEN_ROBOT).draw_text(screen, 825,780)

        # ----------------------Origin Robot----------------------------------
        Text.Text(f'{self._robot}', self._font_text_bar, st.RED_ROBOT).draw_text(screen, 1000,780)