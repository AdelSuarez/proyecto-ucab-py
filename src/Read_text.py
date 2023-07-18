class Read_text:
    def __init__(self) -> None:
        self.open = open('mapa.txt', 'r', encoding='UTF-8')
        print(self.open.read())
        