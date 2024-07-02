class Collision_checker:
    def __init__(self, map_game):
        self.map_game = map_game

    def checker(self) -> str:
        for row in self.map_game:
            for column in row:
                if column == '#':
                    return '#'
                elif column == '@':
                    return '@'
