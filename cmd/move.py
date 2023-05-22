class Move:
    def __init__(self, address, map_game):
        self.address = address
        self.map_game = map_game




    def advance(self):
        # Ciclo que mueve el robot segun la direccion, verificando si se encuentra con colisiones en el camino

        movement_made = False

        for index_row, row in enumerate(self.map_game):
            for index_column, column in enumerate(row):

                if column == '>' and self.address == 'E':
                    # Arroja un error que cuando llega al limite derecho de la lista se inserta el robot en una posicion que no existe. es lo que genera la colision
                    try:
                        if row[index_column+1] == '*':
                            # Verifica si al lado derecho se encuentra una mina, si la hay el robot explota
                            row[index_column] = ' '
                            row[index_column+1] = '#'
                            movement_made = True
                            break
                        elif row[index_column+1] == 'H':
                            # Verifica si al lado derecho se encuentra la meta
                            row[index_column] = ' '
                            row[index_column+1] = '@'
                            movement_made = True
                            break
                        else:
                            # Si no se encnuetra niguna mina o la meta, mueve al robot una casilla a la derecha
                            row[index_column] = ' '
                            row[index_column+1] = '>'
                            movement_made = True
                            break
                    except IndexError:
                        # Si se intenta mover una casilla mas de la que se puede en la lista, va generar un error que esta fuera de rango, que es lo que se usa para detectar la colision 
                        row[index_column] = '#'
                        break

                elif column == '<' and self.address == 'O':
                    if index_column-1 == -1:
                        # Verifica que si llega a la colision de la izquierda y quiere continuar, el robot explota
                        row[index_column] = ' '
                        row[index_column] = '#'
                        movement_made = True
                        break
                    elif row[index_column-1] == '*':
                        # Verifica si al lado izquierdo se encuentra una mina, si la ahi el robot explota
                        row[index_column] = ' '
                        row[index_column-1] = '#'
                        movement_made = True
                        break

                    elif row[index_column-1] == 'H':
                        # Verifica si al lado izquierdo se encuentra una mina, si la ahi el robot explota
                        row[index_column] = ' '
                        row[index_column-1] = '@'
                        movement_made = True
                        break
                    else: 
                        # El robot avanza si no encuentra colision    
                        row[index_column] = ' '
                        row[index_column-1] = '<'
                        movement_made = True
                        break

                elif column == '^' and  self.address == 'N':
                    # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 
                    for j in self.map_game[0]:
                        # El ciclo for verifica si el robot se encuentra en la primera fila con direccion N, y si realiza un movimiento hacia el muro automaticamente el robot explota, pero verifica todo el mapa, aunque no pasa de la primera fila
                        if j == '^':
                            row[index_column] = '#'
                            movement_made = True
                            break

                    if movement_made:
                            # Para cerrar el ciclo y no siga verificando las columnas
                            break
                    if self.map_game[index_row-1][index_column] == '*':
                        # Verifica el lado superior, para saber si ahi un mina, si la ahi el robot explota
                        row[index_column] = ' '
                        self.map_game[index_row-1][index_column] = '#'
                        movement_made = True
                        break

                    elif self.map_game[index_row-1][index_column] == 'H':
                        # Verifica el lado superior, para saber si ahi un mina, si la ahi el robot explota
                        row[index_column] = ' '
                        self.map_game[index_row-1][index_column] = '@'
                        movement_made = True
                        break

                    else:
                        # Mueve el robot si no encuentra colision en direccion N
                        row[index_column] = ' '
                        self.map_game[index_row-1][index_column] = '^'
                        movement_made = True
                        break

                elif column == 'v' and self.address == 'S':
                    # Se vuelven a iterar los bucles para poder mover al robot de lista, se hace en la lista principal 
                    for j in self.map_game[-1]:
                        # El ciclo for verifica si el robot se encuentra en la ultima fila con direccion S, se recorre de nuevo el mapa devido a que se necesita llegar a la ultima fila 
                        if j == 'v':
                            row[index_column] = '#'
                            movement_made = True
                            break

                    if movement_made:
                        break

                    if self.map_game[index_row+1][index_column] == '*':
                        # Verifica el lado inferior, para saber si ahi un mina, si la ahi el robot explota
                        row[index_column] = ' '
                        self.map_game[index_row+1][index_column] = '#'
                        movement_made = True
                        break

                    elif self.map_game[index_row+1][index_column] == 'H':
                        # Verifica el lado inferior, para saber si ahi un mina, si la ahi el robot explota
                        row[index_column] = ' '
                        self.map_game[index_row+1][index_column] = '@'
                        movement_made = True
                        break

                    else:
                        # Mueve el robot si no se ha encontrado en la ultima fila
                        row[index_column] = ' '
                        self.map_game[index_row+1][index_column] = 'v'
                        movement_made = True
                        break

            if movement_made:
            # * Este bucle esta para que los movimineto en N y S no se hagan de manera infinita por los bucles internos 
                break
