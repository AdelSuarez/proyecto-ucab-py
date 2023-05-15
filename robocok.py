# Imports
import os
import random

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
    # TODO list[list][element] -> lo primero es la lista y lo que sigue es el elemento para optimizar luego el codigo
    assests= [' ', '*', 'H', '>']
    # ! Solo muestra el mapa cuando se crea
    # Crear el tamaño del mapa segun los parametros introducidos
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

                
            mapa[i].append(assest)

def verificador_mapa(y, x):
    # recorre el mapa para modificar error con la la ubicacion de la meta y las monas, para evitar gener mapas imposibles de pasar
    a = random.randint(1,3)
    b = random.randint(1,(x-1))

    # TODO verificar cuando el mapa es pequeño, por ejempo 9x3 que se crean bloqueos, de igual formar, verificar la meta que no se bloquee con minas
    # ! Seguir mejorando el verificador del mapa
    for index_fila, fila in enumerate(mapa):
        for index_columna, columna in enumerate(fila):

            if x == 3 or x == 4:
                # verifica si calumna es de estos tamaños, va revisar sicse encuentran tres minas diaginales
                # TODO : eliminar la mina del medio, si se encuentran tres minas seguidas 
                pass 

            if index_fila == 0:
                # verifica si el robot esta en la primera fila y en la primera columna, y si se encuentra rodeado de bombas, elimna la que tiene a la derecha
                if index_columna == 0 and columna == '>':
                    if fila[index_columna+1] == '*' and mapa[index_fila+1][index_columna] == '*':
                        fila[index_columna+1] = ' '

            if (index_fila == 0 or index_fila == 1 or  index_fila == 2) and columna == 'H':
                # Condicional que verifica si la meta se encuantra en las primeras tres filas, si se encuentra la coloca en las ultimas filas del mapa
                fila[index_columna] = ' '
                try:
                    mapa[-a][b] = 'H'
                except Exception:
                    mapa[-a][-1] = 'H'
                        
            
            if columna == '>':
                # verifica si hay dos bombas al lado del robot de derecha e izquierda, elimina la de la parte de la derecha
                try:
                    if fila[index_columna+1] == '*' and fila[index_columna-1] == '*':
                        fila[index_columna+1] = ' '
                except Exception:
                    pass

            if columna == 'H':
                # verifica si hay dos bombas al lado del robot de derecha e izquierda, elimina la de la parte de la derecha
                try:
                    if fila[index_columna+1] == '*' and fila[index_columna-1] == '*':
                        fila[index_columna+1] = ' '
                except Exception:
                    pass

            if columna == '*':
                # elimina las minas que se encuentres dos juntas en las filas impares tanto horizontal como vertical 
                if index_fila%2 == 1:
                    try:
                        if fila[index_columna+1] == '*':
                            fila[index_columna+1] = ' '
                    except Exception:
                        pass
                    try:
                        if mapa[index_fila+1][index_columna] == '*':
                            mapa[index_fila+1][index_columna] = ' '
                    except Exception:
                        pass

                    try:
                        if mapa[index_fila+1][index_columna+1] == '*':
                           mapa[index_fila+1][index_columna+1] = ' '
                    except Exception:
                        pass



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
    movimiento_realizado = False
    for fila in mapa:
        for index, columna in enumerate(fila):
            if columna == '>':
                direccion = 'N'
                fila[index] = '^'
                movimiento_realizado = True
                break

            elif columna == '^':
                direccion = 'O'
                fila[index] = '<'
                movimiento_realizado = True
                break

            elif columna == '<':
                direccion = 'S'
                fila[index] = 'v'
                movimiento_realizado = True
                break

            elif columna == 'v':
                direccion = 'E'
                fila[index] = '>'
                movimiento_realizado = True
                break

        if movimiento_realizado:
            break

    return direccion

def mover_robot_derecha(direccion):
    # Cambia la direccion del robot, solo direccion derecha
    movimiento_realizado = False
    for columna in mapa:
        for index, fila in enumerate(columna):
            if fila == '>':
                direccion = 'S'
                columna[index] = 'v'
                movimiento_realizado = True
                break

            elif fila == 'v':
                direccion = 'O'
                columna[index] = '<'
                movimiento_realizado = True
                break

            elif fila == '<':
                direccion = 'N'
                columna[index] = '^'
                movimiento_realizado = True
                break

            elif fila == '^':
                direccion = 'E'
                columna[index] = '>'
                movimiento_realizado = True
                break
        if movimiento_realizado:
            break

    return direccion


def mover_adelante(direccion, fila_x):
    # Ciclo que mueve el robot segun la direccion, verificando si se encuentra con colisiones en el camino

    movimiento_realizado = False

    for index_fila, fila in enumerate(mapa):
        for index_columna, columna in enumerate(fila):

            if columna == '>' and direccion == 'E':
                # Arroja un error que cuando llega al limite derecho de la lista se inserta el robot en una posicion que no existe. es lo que genera la colision
                try:
                    if fila[index_columna+1] == '*':
                        # Verifica si al lado derecho se encuentra una mina, si la hay el robot explota
                        fila[index_columna] = ' '
                        fila[index_columna+1] = '#'
                        movimiento_realizado = True
                        break
                    elif fila[index_columna+1] == 'H':
                        # Verifica si al lado derecho se encuentra la meta
                        fila[index_columna] = ' '
                        fila[index_columna+1] = '@'
                        movimiento_realizado = True
                        break
                    else:
                        # Si no se encnuetra niguna mina o la meta, mueve al robot una casilla a la derecha
                        fila[index_columna] = ' '
                        fila[index_columna+1] = '>'
                        movimiento_realizado = True
                        break
                except IndexError:
                    # Si se intenta mover una casilla mas de la que se puede en la lista, va generar un error que esta fuera de rango, que es lo que se usa para detectar la colision 
                    fila[index_columna] = '#'
                    break

            elif columna == '<' and direccion == 'O':
                if index_columna-1 == -1:
                    # Verifica que si llega a la colision de la izquierda y quiere continuar, el robot explota
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

            elif columna == '^' and  direccion == 'N':
                # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 
                for j in mapa[0]:
                    # El ciclo for verifica si el robot se encuentra en la primera fila con direccion N, y si realiza un movimiento hacia el muro automaticamente el robot explota, pero verifica todo el mapa, aunque no pasa de la primera fila
                    if j == '^':
                        fila[index_columna] = '#'
                        movimiento_realizado = True
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

            elif columna == 'v' and direccion == 'S':
                # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 
                for j in mapa[fila_x-1]:
                    # El ciclo for verifica si el robot se encuentra en la ultima fila con direccion S, se recorre de nuevo el mapa devido a que se necesita llegar a la ultima fila 
                    if j == 'v':
                        fila[index_columna] = '#'
                        movimiento_realizado = True
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
                return '#'
            elif columna == '@':
                return '@'

def posicion_robot():
    # * Muestra la ubicacion del robot en tiempo real 
    posicion_fila_r = 0
    posicion_column_r = 0

    posicion_robot  = False
    for  index_fila ,fila in enumerate(mapa):
        for index_columna , value in enumerate(fila):
            if value == '>' or value == '<' or value == 'v' or value == '^':
                posicion_fila_r = index_fila+1
                posicion_column_r = index_columna+1
                posicion_robot = True
                break              
        if posicion_robot:
            break

    return (posicion_fila_r, posicion_column_r)

def posicion_meta():
    # se busca la ubicacion de la meta de forma independiente debido a que esta funcion solo se va llamar una vez
    posicion_fila_m = 0
    posicion_column_m = 0
    posicion_meta  = False

    for  index_fila ,fila in enumerate(mapa):
        for index_columna , value in enumerate(fila):
            if value == 'H':
                posicion_fila_m = index_fila+1
                posicion_column_m = index_columna+1
                posicion_meta = True
                break                    
        if posicion_meta:
            break

    return ( posicion_fila_m, posicion_column_m)


def datos_mapa():
    # Varibles para colocar el mensaje sobre el mapa
    mensaje_activo = False
    mensaje = None

    while True:
        # Ciclo que verifica los valores para la creacion del mapa, se cierra luego de comprobar que todos los valores son correctos 

        limpiar_consola()
        print('BIENVENIDO'.center(40, '-'))

        try: 
            # Excepcion que validad si los valores que se han introducidos son validos para poder continuar, verifica si en la creacion del tamaño del mapa, si los parametros son letras y no numeros va arrojar mensajes, y solo continuara la ejecucion de programa solo hasta que se introduzcan numeros

            if mensaje_activo:
                # Condicion que imprime el mesaje del mapa si se coloca datos incorrectos 
                print(mensaje.center(40,' '))

            print('\nTamaño del mapa que deceas crear: ')
            y = int(input('introduce la cantidad de columnas >> '))
            x = int(input('Introduce la cantidad de filas >> '))
            
            if (x >= 4  and y >= 3) or (x >= 3  and y >= 4):
                break
            else:
                mensaje_activo = True
                mensaje='*Tamaño del mapa insuficiente*'

        except Exception:
            mensaje = '*No se aceptan letras*'
            mensaje_activo = True
    
    return (y, x)

def fin_juego(contador, verificador, y):
    limpiar_consola()
    mostrar_mapa(y)
    print('')
    print('FIN DEL JUEGO'.center((y*4)+3, '-'))
    if contador > 40:
        print('\n>> Perdiste\n>> Movientos agotados\n')
    elif verificador == '#':
        print('\n>> Perdiste\n>> El robot a colisionado o tocado una mina\n')
    elif verificador == '@':
        print(f'\n>> Ganaste\n>> Realizaste {contador} movimientos para llegar a la meta\n')


def Manager():

    # Variables 
    direccion = 'E'
    contador_ordenes = 0

    (y, x) =  datos_mapa()
    crear_mapa(x, y)
    verificador_mapa(y, x)
    (posicion_y_m, posicion_x_m) = posicion_meta()
    
    while True:


        (posicion_x_r, posicion_y_r) = posicion_robot()
        limpiar_consola()

        print(f' C: {y} | F: {x} '.center((y*4)+3,'-'))
        print('')
        mostrar_mapa(y)

        print(f'\nPosicion de robot >> C: {posicion_x_r} | F: {posicion_y_r}\nPosicion de la meta >> C: {posicion_x_m} | F: {posicion_y_m} \nv1.0.1')
        
        print(f'''
    N     | Ordenes: {contador_ordenes}
    ↑     ---------------------------    
O ← {direccion} → E | A >> Avanzar
    ↓     | I >> Mover a la Izquierda
    S     | D >> Mover a la Derecha
''')
        
        # ! Cierra el ciclo principal debido a que supero las ordenes extablecidas
        if contador_ordenes > 40:
            fin_juego(contador_ordenes, verificador_colision(), y)
            break
        # ! Cierra el ciclo principal debido a que el robot perdio
        if verificador_colision() == '#' or verificador_colision() == '@' :
            fin_juego(contador_ordenes, verificador_colision(), y)
            break

        movimiento = input('Introduce el movimiento >> ')

        # * Condicional que realiza el cambio de la direccion del robot en el mapa 
        if movimiento.lower().strip() == 'i':
            contador_ordenes +=1
            direccion = mover_robot_izquierda(direccion)

        elif movimiento.lower().strip() == 'd':
            contador_ordenes +=1
            direccion = mover_robot_derecha(direccion)

        elif movimiento.lower().strip() == 'a':
            contador_ordenes +=1
            mover_adelante(direccion, x)


if __name__ == '__main__':
    Manager()
