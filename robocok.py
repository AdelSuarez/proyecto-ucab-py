# Imports
import time
import sys
import os
import random
import sqlite3


# ! Recordatorios para saber que voy bien
# TODO: Arreglar los error de datos, he implementar exception en las variables de entradas para evitar error de tipado
# ! Preguntar la profesor si se puede hacer el codigo asi
# TODO: Implementar una base de datos en sqlite para guardar los records de los jugadores

# Variable que almacena el tamaño del mapa establecida al pricipio para tener acceso global
mapa = []


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
  
    str_carga = "iniciando juego..."
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

    assests= [0, '*', 'H', '>']
    # ! Solo muestra el mapa cuando se crea
    # Crear el tamaño del mapa segun los parametros introducidos
    robot = 0
    meta = 0
    # TODO: arreglar, la meta no este cerca de el robot y que no se bloquee el camino con las minas
    for i in range(x):
        # Ciclo que crea las filas
        mapa.append([])
        for j in range(y):
            while True:
                # Selecciona un assest al azar de la lista para crear mapas aleatorios
                assest = random.choice(assests)
                if assest != '>' and assest != 'H':
                    break
                elif robot == 0:
                    if assest == '>':
                        robot +=1
                        break
                elif meta == 0:
                    if assest == 'H':
                        meta +=1
                        break
                
            mapa[i].append(assest)

            



# def crear_mapa(x, y):
      # ! No borrar hasta arreglar los mapas aleatorios 
#     # ! Solo muestra el mapa cuando se crea y es el mapa de ejemplo
#     # Crear el tamaño del mapa segun los parametros introducidos
#     for i in range(x):
#         # Ciclo que crea las filas
#         map.append([])
#         for j in range(y):
#             # Ciclo que crea las columnas
#             if (j == 1 or j == 2) and i == 0 :
#                 if j == 1:
#                     # Colocando las bombas de la primera fila
#                     map[i].append('*')
#                 elif j == 2 and i == 0:
#                     map[i].append('H')
#             elif (j == 0 or j == 2 or j == 3 or j== 1) and i == 1:

#                 if j==1:
#                     # Colocando al robot
#                     map[i].append('>')
#                 else:
#                     # Colocando las bombas de la segunda fila
#                     map[i].append('*')
#             elif j == 2 and i == 2:
#                 # Colocando las bombas de la tercera fila
#                 map[i].append('*')
#             else:
#                 map[i].append(0)


def mostrar_mapa(y):
    # variable que lleva el conteo para saber cuando es la ultima fila y colocar los |
    count = 1
    for i in range(len(mapa)):
        # Print que crea la linea superior del mapa 
        print(''.center((y*4)+1,'-'))

        # Ciclos que imprime el mapa sin los [] de las listas
        for j in mapa[i]:
            if count < y:
                print(f'| {j} ', end='')
                count+=1
            elif count == y:
                print(f'| {j} |', end='')
                count = 1

        print('')
    # Print que crea la linea inferior del mapa 
    print(''.center((y*4)+1,'-'))


def mover_robot_I(d):
    # Cambia la direccion del robot, solo direccion izquierda
    for i in mapa:
        # print(i)
        for count, j in enumerate(i):
            if j == '>':
                if d == 'N':
                    i[count] = '^'

            elif j == '^':
                if d == 'O':
                    i[count] = '<'

            elif j == '<':
                if d == 'S':
                    i[count] = 'v'

            elif j == 'v':
                if d == 'E':
                    i[count] = '>'


def mover_robot_D(d):
    # Cambia la direccion del robot, solo direccion derecha
    for i in mapa:
        # print(i)
        for count, j in enumerate(i):
            if j == '>':
                if d == 'S':
                    i[count] = 'v'
            elif j == 'v':
                if d == 'O':
                    i[count] = '<'

            elif j == '<':
                if d == 'N':
                    i[count] = '^'

            elif j == '^':
                if d == 'E':
                    i[count] = '>'


                
        # ! No borrar hasta que el movimiento y las colisiones funcionen
        # for j in map[i]:
        #     print(j)
            # if j == '>':
            #     if d == 'N':
            #         print(j)
            #         map[count] = '^'
            #         count += 1
            #         print(j)
            #         print(map)

            # else:
            #     print(j)

            #     # map[count] = j
            #     count += 1

def mover_adelante(d):
    # ! arreglar las colisiones del mapa
    # TODO: Implementar de cuando se toque una mina, el robot pierde 

    movimiento_realizado = False
    for count, i in enumerate(mapa):
        # print(i)
        for count_list, j in enumerate(i):
            if j == '>':
                if d == 'E':
                    # La unica colision que funciona por los momentos
                    # Arroja un error ya que cuando llega al limite derecho de la lista se inserta el robot en una posicion que no existe. es lo que genera la colision
                    try:
                        i[count_list] = ' '
                        i[count_list+1] = '>'
                        movimiento_realizado = True

                        break
                    except IndexError:
                        i[count_list] = '#'
                        break
            elif j == '<':
                if d == 'O':
                    i[count_list] = ' '
                    i[count_list-1] = '<'
                    movimiento_realizado = True
                    
                    break

            elif j == '^':
                if d == 'N':
                    # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 

                    for x,l in enumerate(mapa):
                        if x == count-1:
                            i[count_list] = ' '
                            print(x, l)
                            l[count_list] = '^'
                            movimiento_realizado = True
                            break

            elif j == 'v':
                if d == 'S':
                    # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 
                    for x,l in enumerate(mapa):
                        if x == count+1:
                            i[count_list] = ' '
                            l[count_list] = 'v'
                            movimiento_realizado = True
                            break
        # * Este bucle esta para que los movimineto en N y S no se hagan de manera infinita por los bucles internos 
        if movimiento_realizado:
            break

def verificador_colision():
    # Itera el mapa completo para saber si el robot a tocado alguna mira o pared, busca el simbolo # que hace la representacion del robot dañado  
    for i in mapa:
        for j in i:
            if j == '#':
                return True

def posicion():
    # TODO: Arreglar la ubicacion del robot ya que muestra es el tamaño  del mapa
    x = 0
    y = 0
    posicion  = False
    for i in range(len(mapa)):
        for count_y, j in enumerate(i):
            if j == '>':
                print(i)
                print(count_y)

                y = count_y
                x = i
                posicion = True                
                break
        if posicion:
            break

    return (x, y)




def Manager():

    animacion()
    (x, y) = posicion()
    # Variables 
    D = 'E'
    contador_ordenes = 0
    

    print('BIENVENIDO'.center(40, '-'))
    y = int(input('introduce la cantidad de columnas >> '))
    x = int(input('Introduce la cantidad de filas >> '))
    # Condicional que verifica que sea un rectangulo horizontal
    crear_mapa(x, y)
    while True:
        limpiar_consola()

        print(f' C: {y} | F: {x} '.center((y*4)+1,'-'))
        mostrar_mapa(y)

        print(f'Posicion de robot >> x | y')
        print('Posicion de la meta >> X | Y')

        print(f'''
N     | Ordenes: {contador_ordenes}
↑     ---------------------------    
O ← {D} → E | A >> Avanzar
↓     | I >> Mover a la Izquierda
S     | D >> Mover a la Derecha
''')
        
        # ! Cierra el ciclo principal debido a que supero las ordenes extablecidas
        if contador_ordenes == 40:
            break
        # ! Cierra el ciclo principal debido a que el robot perdio
        if verificador_colision():
            break


        movimiento = input('Introduce el movimiento >> ')


        # * Condicional que realiza el cambio de la direccion del robot en el mapa 
        if movimiento == 'i':
            if D == 'E':
                D = 'N'
                mover_robot_I(D)
                contador_ordenes +=1
            elif D == 'N':
                D = 'O'
                mover_robot_I(D)
                contador_ordenes +=1

            elif D == 'O':
                D = 'S'
                mover_robot_I(D)
                contador_ordenes +=1

            else:
                D = 'E'
                mover_robot_I(D)
                contador_ordenes +=1

        elif movimiento == 'd':
            if D == 'E':
                D = 'S'
                mover_robot_D(D)
                contador_ordenes +=1

            elif D == 'S':
                D = 'O'
                mover_robot_D(D)
                contador_ordenes +=1

            elif D == 'O':
                D = 'N'
                mover_robot_D(D)
                contador_ordenes +=1

            else:
                D = 'E'
                mover_robot_D(D)
                contador_ordenes +=1
        elif movimiento == 'a':
            contador_ordenes +=1

            mover_adelante(D)


if __name__ == '__main__':
    Manager()
