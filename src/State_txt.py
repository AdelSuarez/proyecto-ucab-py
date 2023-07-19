class State_text:
    def __init__(self, state) -> None:
        self.state = state


        with open('mapa_finally.txt', 'w') as self.file:
            self.file.write(f'{self.state}')