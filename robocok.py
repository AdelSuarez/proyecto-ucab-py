# Imports
import time
import sys
import os

# Variable que almacena el tamaño del mapa
map = []

# * Limpia la consola segun el sistema
def limpiar_consola():
    # windows
    if os.name =="nt":
        os.system("cls")
          
    # linux
    else:
        os.system("clear")

# ! No documentar...
def animacion():
  
    str_carga = "Iniciando juego..."
    str_len = len(str_carga)
  
  
    carga = "|/-\\"
    contador = 0

    contador_tiempo = 0        
      
    i = 0                     
  
    while (contador_tiempo != 20):
          
        time.sleep(0.075) 
                              
        str_carga_list = list(str_carga) 
          
        x = ord(str_carga_list[i])
          
        y = 0                             
  
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            str_carga_list[i]= chr(y)
          
        res =''             
        for j in range(str_len):
            res = res + str_carga_list[j]
              
        sys.stdout.write("\r"+res + carga[contador])
        sys.stdout.flush()
  
        str_carga = res
  
        contador = (contador + 1)% 4
        i =(i + 1)% str_len
        contador_tiempo = contador_tiempo + 1

    limpiar_consola()
      

def crear_mapa(x, y):
    # ! Solo muestra el mapa cuadno se crea
    # Crear el tamaño del mapa segun los parametros introducidos
    for i in range(x):
        # Ciclo que crea las filas
        map.append([])
        for j in range(y):
            # Ciclo que crea las columnas
            if (j == 1 or j == 2) and i == 0 :
                if j == 1:
                    # Colocando las bombas de la primera fila
                    map[i].append('*')
                elif j == 2 and i == 0:
                    map[i].append('H')
            elif (j == 0 or j == 2 or j == 3 or j== 1) and i == 1:

                if j==1:
                    # Colocando al robot
                    map[i].append('>')
                else:
                    # Colocando las bombas de la segunda fila
                    map[i].append('*')
            elif j == 2 and i == 2:
                # Colocando las bombas de la tercera fila
                map[i].append('*')
            else:
                map[i].append(0)


def mostrar_mapa(y):
    # variable que lleva el conteo para saber cuando es la ultima fila y colocar los |
    count = 1
    for i in range(len(map)):
        # Print que crea la linea superior del mapa 
        print(''.center((y*4)+1,'-'))

        # Ciclos que imprime el mapa sin los [] de las listas
        for j in map[i]:
            if count < y:
                print(f'| {j} ', end='')
                count+=1
            elif count == y:
                print(f'| {j} |', end='')
                count = 1

        print('')
    # Print que crea la linea inferior del mapa 
    print(''.center((y*4)+1,'-'))
           

def Manager():
    animacion()
    
    print('BIENVENIDO'.center(40, '-'))
    y = int(input('introduce la cantidad de columnas >> '))
    x = int(input('Introduce la cantidad de filas >> '))

    # Condicional que verifica que sea un rectangulo horizontal
    if y > x:
        crear_mapa(x, y)
        limpiar_consola()
        print(f' C: {y} | F: {x} '.center((y*4)+1,'-'))
        mostrar_mapa(y)
    else:
        print('Las columnas no puedes ser menores a las filas')






if __name__ == '__main__':
    Manager()

        


