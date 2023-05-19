import style.style as st

class View_map:
    count = 1
    position = 1
    
    def __init__(self,row, map_game) -> None:
        self._row = row
        self.map_game = map_game


    def view(self):
        # variable que lleva el conteo para saber cuando es la ultima fila y colocar los |
        character_count = (self._row*4)+1
        print('  ', end='')
        for i in range(self._row):
            if i+1 >= 10:
                print(f'  {st.BLUE}{i+1}{st.RESET}', end='')
            else:
                print(f'  {st.BLUE}{i+1}{st.RESET} ', end='')

        
        print('')
        for i in range(len(self.map_game)):
            # Print que crea la linea superior del mapa 
            print('  ', end='')
            print(''.center(character_count,'-'))
            view_number = True
            # Ciclos que imprime el mapa sin los [] de las listas
            for j in self.map_game[i]:
                # TODO: optimizar el codigo
                if view_number:
                    if View_map.position >= 10:
                        print(f'{st.BLUE}{View_map.position}{st.RESET}', end='')
                    else:
                        print(f'{st.BLUE}{View_map.position}{st.RESET} ', end='')
                    View_map.position+=1

                if View_map.count < self._row:
                    if j ==  '>' or j ==  '<' or j ==  '^' or j ==  'v': 
                        print(f'| {st.GREEN}{j}{st.RESET} ', end='')
                        view_number=False
                        View_map.count+=1
                    elif j == '*' or j=='#':
                        print(f'| {st.RED}{j}{st.RESET} ', end='')
                        view_number=False
                        View_map.count+=1

                    elif j == 'H':
                        print(f'| {st.YELLOW}{j}{st.RESET} ', end='')
                        view_number=False
                        View_map.count+=1
                    else:
                        print(f'| {j} ', end='')
                        view_number=False
                        View_map.count+=1
                elif View_map.count == self._row:
                    if j ==  '>' or j ==  '<' or j ==  '^' or j ==  'v': 
                        print(f'| {st.GREEN}{j}{st.RESET} |', end='')
                        View_map.count = 1
                    elif j == '*' or j=='#':
                        print(f'| {st.RED}{j}{st.RESET} |', end='')
                        View_map.count = 1
                    elif j == 'H':
                        print(f'| {st.YELLOW}{j}{st.RESET} |', end='')
                        View_map.count = 1
                    else:
                        print(f'| {j} |', end='')
                        View_map.count = 1


            print('')
        # Print que crea la linea inferior del mapa 
        print('  ', end='')
        print(''.center(character_count,'-'))