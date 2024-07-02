from screen.main_screen import Main_screen


class Manager:

    # * Tareas:
    # ! Esta clase esta por la razon de que estaba unida con la app de terminal
    # TODO: eliminar la clase o cambiar en un futuro
    # TODO: Implementar el movimiento automatico, pero sera en vacaciones
    # TODO: Implementar que se pueda volver a jugar (En proceso)

    def __init__(self):
        self.views()

    def views(self):
        Main_screen()
