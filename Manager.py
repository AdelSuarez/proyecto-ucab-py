from src.cmd.main_menu import Main_menu
# from src.screen.main_screen import main
class Manager:

    def __init__(self):
        self.views()
    

    def views(self):
        # print('BIENVENIDO')
        # print('1 | Jugar la version de terminal')
        # print('2 | Jugar la version de grafica')

        # option = int(input('Introduce la opcion >> '))
        # if option == 1:
        Main_menu()
        # elif option == 2:
            # main()
            # print('grafica')