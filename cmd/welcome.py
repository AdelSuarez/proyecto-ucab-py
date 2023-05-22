import style.style as st
from src.clear_terminal import clear

class Data_map:
    is_message = False
    message = None


    def welcome(self):

        while True:
            # Ciclo que verifica los valores para la creacion del mapa, se cierra luego de comprobar que todos los valores son correctos 
            clear()
            print('BIENVENIDO'.center(40, '-'))
            try: 
                # Excepcion que validad si los valores que se han introducidos son validos para poder continuar, verifica si en la creacion del tamaño del mapa, si los parametros son letras y no numeros va arrojar mensajes, y solo continuara la ejecucion de programa solo hasta que se introduzcan numeros

                if Data_map.is_message:
                    # Condicion que imprime el mesaje del mapa si se coloca datos incorrectos 
                    print(Data_map.message.center(40,' '))

                print('\nTamaño del mapa que deseas crear: ')
                column = int(input(f'introduce la cantidad de columnas {st.GREEN}>>{st.RESET} '))
                row = int(input(f'Introduce la cantidad de filas {st.GREEN}>>{st.RESET} '))
                
                if (column >= 4  and row >= 3) or (column >= 3  and row >= 4):
                    break
                else:
                    Data_map.is_message = True
                    Data_map.message=f'*Tamaño del mapa insuficiente*'

            except Exception:
                Data_map.message = '*No se aceptan letras*'
                Data_map.is_message = True
        
        return (row, column)

