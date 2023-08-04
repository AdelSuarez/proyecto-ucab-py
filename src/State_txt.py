class StateText:
    def __init__(self, state) -> None:
        self.state = state

        with open('mapa_final.txt', 'w') as self.file:
            if self.state == '#':
                self.file.write('N')
            elif self.state == '@':
                self.file.write('Y')
