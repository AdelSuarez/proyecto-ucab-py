# Imports
import os
import random

# TODO: Arreglar los error de datos, he implementar exception en las variables de entradas para evitar error de tipado
# ! Preguntar la profesor si se puede hacer el codigo asi

# Variable que almacena el tamaño del mapa, establecida al pricipio para tener acceso global
mapa = []

# * Limpia la consola segun el sistema
def limpiar_consola():
    # windows
    if os.name =="nt":
        os.system("cls")
          
    # linux
    else:
        os.system("clear")
      

def crear_mapa(x, y):
    # ! list[list][element] -> lo primero es la lista y lo que sigue es el elemento para optimizar luego el codigo
    assests= [' ', '*', 'H', '>']
    # ! Solo muestra el mapa cuando se crea
    # Crear el tamaño del mapa segun los parametros introducidos
    # contador_minas = 0
    robot = True
    meta = True
    for i in range(x):
        # Ciclo que crea las filas
        mapa.append([])
        for j in range(y):
            while True:
                # Selecciona un assest al hazar de la lista para crear mapas aleatorios
                assest = random.choice(assests)
                if assest != '>' and assest != 'H':
                    break
                elif robot :
                    if assest == '>':
                        robot = False
                        break
                elif meta:
                    if assest == 'H':
                        meta = False
                        break

                # elif contador_minas < ((y*x)) - ((y+x)*3) :
                #     if assest == '*':
                #         contador_minas +=1 
                #         break

                
            mapa[i].append(assest)

def verificador_mapa(y, x):
    # recorre el mapa para modificar error con la la ubicacion de la meta y las monas, para evitar gener mapas imposibles de pasar
    # TODO Verificar la ubicacion de las minas
    # a = random.randint(-1,-3)
    b = random.randint(0,(x-1))
    contador_minas = 0
    for index_fila, fila in enumerate(mapa):
        for index_columna, columna in enumerate(fila):

            if index_fila == 0 or index_fila == 1 or  index_fila == 2:
                # Condicional que verifica si la meta se encuantra en las primeras tres filas, si se encuentra la coloca en las ultimas filas del mapa
                if columna == 'H':
                    fila[index_columna] = ' '
                    try:
                        mapa[-1][b] = 'H'
                    except Exception:
                        pass

            if columna == '*':
                try:
                    if mapa[index_fila][index_columna+1] == '*':
                        mapa[index_fila][index_columna+1] = ' '
                    
                    if mapa[index_fila+1][index_columna] == '*':
                        mapa[index_fila+1][index_columna] = ' '
                    
                except Exception:
                    pass

            # if index_fila == a:
            #     # Condicional que verifica la ubicacion de la meta, previamente recolocada, donde se verifica si a sus alrededores se encuantran muchas mina, donde elimina si bloquea la meta  
            #     if columna == 'H':
            #         # Verifica las filas de la parte superior e inferior
            #         if mapa[index_fila-1][index_columna] == '*':
            #             mapa[index_fila-1][index_columna] = 'X'
            #             contador_minas +=1
            #         try:    
            #             if mapa[index_fila+1][index_columna] == '*':
            #                 mapa[index_fila+1][index_columna] = 'X'
            #                 contador_minas +=1
            #         except Exception:
            #             pass

            #         # Verifica las columnas de la parte derecha e izquierda
            #         if fila[index_columna+1] == '*':
            #             fila[index_columna+1] = 'X'
            #             contador_minas +=1

            #         try:
            #             if fila[index_columna-1] == '*':
            #                 fila[index_columna-1] = 'X'
            #                 contador_minas +=1
            #         except Exception:
            #             pass

                # if contador_minas > 2:
                #         mapa[index_fila-1][index_columna] = 'X'
                #         mapa[index_fila+1][index_columna] = 'X'
                #         fila[index_columna+1] = 'X'
                #         fila[index_columna-1] = 'X'






                

                # if columna[index_columna+1] == '*':
                #     columna[index_columna+1] = ' '
                # elif columna[index_columna-1] == '*':
                #     columna[index_columna-1] = ' '



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
    posicion = 1
    cantidad_caracter = (y*4)+1
    print('  ', end='')
    for i in range(y):
        if i+1 >= 10:
            print(f'  {i+1}', end='')
        else:
            print(f'  {i+1} ', end='')

    
    print('')
    for i in range(len(mapa)):
        # Print que crea la linea superior del mapa 
        print('  ', end='')
        print(''.center(cantidad_caracter,'-'))
        numero = True
        # Ciclos que imprime el mapa sin los [] de las listas
        for j in mapa[i]:
            if numero:
                if posicion >= 10:
                    print(f'{posicion}', end='')
                else:
                    print(f'{posicion} ', end='')
                posicion+=1

            if count < y:
                print(f'| {j} ', end='')
                numero=False
                count+=1
            elif count == y:
                print(f'| {j} |', end='')
                count = 1


        print('')
    # Print que crea la linea inferior del mapa 
    print('  ', end='')
    print(''.center(cantidad_caracter,'-'))


def mover_robot_izquierda(direccion):
    # Cambia la direccion del robot, solo direccion izquierda
    for fila in mapa:
        for index, columna in enumerate(fila):
            if columna == '>':
                direccion = 'N'
                fila[index] = '^'

            elif columna == '^':
                direccion = 'O'
                fila[index] = '<'

            elif columna == '<':
                direccion = 'S'
                fila[index] = 'v'

            elif columna == 'v':
                direccion = 'E'
                fila[index] = '>'

    return direccion

def mover_robot_derecha(direccion):
    # Cambia la direccion del robot, solo direccion derecha
    for columna in mapa:
        for index, fila in enumerate(columna):
            if fila == '>':
                direccion = 'S'
                columna[index] = 'v'

            elif fila == 'v':
                direccion = 'O'
                columna[index] = '<'

            elif fila == '<':
                direccion = 'N'
                columna[index] = '^'

            elif fila == '^':
                direccion = 'E'
                columna[index] = '>'

    return direccion


def mover_adelante(direccion, fila_x):
    # Ciclo que mueve el robot segun la direccion, verificando si se encuentra con colisiones en el camino
    # TODO: Implementar de cuando se toque una mina, el robot pierde 

    movimiento_realizado = False
    for index_fila, fila in enumerate(mapa):
        for index_columna, columna in enumerate(fila):

            if columna == '>':
                if direccion == 'E':
                    # Arroja un error que cuando llega al limite derecho de la lista se inserta el robot en una posicion que no existe. es lo que genera la colision
                    try:
                        if fila[index_columna+1] == '*':
                            # Verifica si al lado derecho se encuentra una mina, si la ahi el robot explota
                            fila[index_columna] = ' '
                            fila[index_columna+1] = '#'

                            break
                        elif fila[index_columna+1] == 'H':
                            fila[index_columna] = ' '
                            fila[index_columna+1] = '@'
                            break
                        else:
                            fila[index_columna] = ' '
                            fila[index_columna+1] = '>'
                            movimiento_realizado = True
                            break
                    except IndexError:
                        fila[index_columna] = '#'
                        break

            elif columna == '<':
                if direccion == 'O':
                    if index_columna-1 == -1:
                        #Condicion que verifica que si llega a la colision de la izquierda y quiere continuar, el robot explota
                        fila[index_columna] = ' '
                        fila[index_columna-1] = '#'
                        movimiento_realizado = True
                        break
                    elif fila[index_columna-1] == '*':
                        # Verifica si al lado izquierdo se encuentra una mina, si la ahi el robot explota
                        fila[index_columna] = '#'
                        movimiento_realizado = True
                        break

                    elif fila[index_columna-1] == 'H':
                        # Verifica si al lado izquierdo se encuentra una mina, si la ahi el robot explota
                        fila[index_columna] = ' '
                        fila[index_columna-1] = '@'
                        movimiento_realizado = True
                        break
                    else: 
                        # El robot avanza si no encuentra colision    
                        fila[index_columna] = ' '
                        fila[index_columna-1] = '<'
                        movimiento_realizado = True
                        break

            elif columna == '^':
                if direccion == 'N':
                    # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 
                    for i,f in enumerate(mapa):
                        if i == 0:
                            for j in f:
                                # El ciclo for verifica si el robot se encuentra en la primera fila con direccion N, y si realiza un movimiento hacia el muro automaticamente el robot explota, pero verifica todo el mapa, aunque no pasa de la primera fila
                                if j == '^':
                                    fila[index_columna] = '#'
                                    movimiento_realizado = True
                                    break

                        if movimiento_realizado:
                            # Para cerrar el ciclo y no siga verificando las columnas
                            break
                        
                    if movimiento_realizado:
                            # Para cerrar el ciclo y no siga verificando las columnas
                            break
                    if mapa[index_fila-1][index_columna] == '*':
                        # Verifica el lado superior, para saber si ahi un mina, si la ahi el robot explota
                        fila[index_columna] = ' '
                        mapa[index_fila-1][index_columna] = '#'
                        movimiento_realizado = True
                        break

                    elif mapa[index_fila-1][index_columna] == 'H':
                        # Verifica el lado superior, para saber si ahi un mina, si la ahi el robot explota
                        fila[index_columna] = ' '
                        mapa[index_fila-1][index_columna] = '@'
                        movimiento_realizado = True
                        break

                    else:
                        # Mueve el robot si no encuentra colision en direccion N
                        fila[index_columna] = ' '
                        mapa[index_fila-1][index_columna] = '^'
                        movimiento_realizado = True
                        break

            elif columna == 'v':
                if direccion == 'S':
                    # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 
                    for i , f in enumerate(mapa):
                        if i == fila_x-1:
                            # La condicion lo que hace es que solo se verifique que se encuentra en la ultima columna de la lista
                            for j in f:
                                # El ciclo for verifica si el robot se encuentra en la ultima fila con direccion S, se recorre de nuevo el mapa devido a que se necesita llegar a la ultima fila 
                                if j == 'v':
                                    fila[index_columna] = '#'
                                    movimiento_realizado = True
                                    break
                            if movimiento_realizado:
                                # Cierra el ciclo para que no siga verifcando
                                break

                    if movimiento_realizado:
                        break

                    if mapa[index_fila+1][index_columna] == '*':
                        # Verifica el lado inferior, para saber si ahi un mina, si la ahi el robot explota
                        fila[index_columna] = ' '
                        mapa[index_fila+1][index_columna] = '#'
                        movimiento_realizado = True
                        break

                    elif mapa[index_fila+1][index_columna] == 'H':
                        # Verifica el lado inferior, para saber si ahi un mina, si la ahi el robot explota
                        fila[index_columna] = ' '
                        mapa[index_fila+1][index_columna] = '@'
                        movimiento_realizado = True
                        break

                    else:
                        # Mueve el robot si no se ha encontrado en la ultima fila
                        fila[index_columna] = ' '
                        mapa[index_fila+1][index_columna] = 'v'
                        movimiento_realizado = True
                        break

        if movimiento_realizado:
        # * Este bucle esta para que los movimineto en N y S no se hagan de manera infinita por los bucles internos 
            break

def verificador_colision():
    # Itera el mapa completo para saber si el robot a tocado alguna mina o pared, busca el simbolo # que hace la representacion del robot dañado  
    for fila in mapa:
        for columna in fila:
            if columna == '#':
                return True
            elif columna == '@':
                return True

def posicion():
    # * Muestra la ubicacion del robot en tiempo real y la de la meta 
    posicion_fila_r = 0
    posicion_column_r = 0
    posicion_fila_m = 0
    posicion_column_m = 0

    posicion_meta  = False
    posicion_robot  = False
    for  index_fila ,fila in enumerate(mapa):
        for index_columna , value in enumerate(fila):
            if value == 'H':
                posicion_fila_m = index_fila+1
                posicion_column_m = index_columna+1
                posicion_meta = True
            if value == '>' or value == '<' or value == 'v' or value == '^':
                posicion_fila_r = index_fila+1
                posicion_column_r = index_columna+1
                posicion_robot = True                
        if posicion_robot and posicion_meta:
            break

    return (posicion_fila_r, posicion_column_r, posicion_fila_m, posicion_column_m)


def Manager():

    # Variables 
    direccion = 'E'
    contador_ordenes = 0
    
    # Varibles para colocar el mensaje sobre el mapa
    mensaje_activo = False
    mensaje = None

    while True:
        # Ciclo que verifica los valores para la creacion del mapa, se cierra luego de comprobar que todos los valores son correctos 

        limpiar_consola()
        print('BIENVENIDO'.center(40, '-'))


        try:
            if mensaje_activo:
                # Condicion que imprime el mesaje del mapa si se coloca datos incorrectos 
                print(mensaje.center(40,' '))

            print('\nTamaño del mapa que deceas crear: ')
            y = int(input('introduce la cantidad de columnas >> '))
            x = int(input('Introduce la cantidad de filas >> '))
            
            if x != y:
                if (x >= 4  and y >= 3) or (x >= 3  and y >= 4):
                    break
                else:
                    mensaje_activo = True
                    mensaje='*Tamaño del mapa insuficiente*'
            else:
                mensaje_activo = True
                mensaje='*Los valores no pueden ser iguales*'

        except Exception:
            mensaje = '*No se aceptan letras*'
            mensaje_activo = True
        # Condicional que verifica el tamaño del mapa 

    crear_mapa(x, y)
    verificador_mapa(y, x)
    
    while True:
        (posicion_x_r, posicion_y_r, posicion_x_m, posicion_y_m) = posicion()
        limpiar_consola()

        print(f' C: {y} | F: {x} '.center((y*4)+3,'-'))
        print('')
        mostrar_mapa(y)
        print('')
        print(f'Posicion de robot >> C: {posicion_x_r} | F: {posicion_y_r}')
        print(f'Posicion de la meta >> C: {posicion_x_m} | F: {posicion_y_m}')
        print('v0.1.9')
        print(f'''
    N     | Ordenes: {contador_ordenes}
    ↑     ---------------------------    
O ← {direccion} → E | A >> Avanzar
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
        if movimiento.lower().strip() == 'i':
            direccion = mover_robot_izquierda(direccion)

        elif movimiento.lower().strip() == 'd':
            direccion = mover_robot_derecha(direccion)
            contador_ordenes +=1

        elif movimiento.lower().strip() == 'a':
            contador_ordenes +=1
            mover_adelante(direccion, x)


if __name__ == '__main__':
    Manager()
    print('Fin del juego')
