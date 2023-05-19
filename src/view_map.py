import style.style as st

class View_map:
    count = 1
    position = 1
    
    def __init__(self,row, map_game) -> None:
        self._row = row
        self.map_game = map_game


    def view(self):

        self._number_up()
        
        for i in range(len(self.map_game)):
            
            # Print que crea la linea superior del mapa 
            self._separator_line()

            view_number = True

            # Ciclos que imprime el mapa sin los [] de las listas
            for j in self.map_game[i]:

                # TODO: optimizar el codigo
                self._number_left(view_number)

                if View_map.count < self._row:
                    if j ==  '>' or j ==  '<' or j ==  '^' or j ==  'v': 
                        self._view_assest(j, st.GREEN)
                        view_number=False

                    elif j == '*' or j=='#':
                        self._view_assest(j, st.RED)
                        view_number=False

                    elif j == 'H':
                        self._view_assest(j, st.YELLOW)
                        view_number=False

                    else:
                        print(f'| {j} ', end='')
                        view_number=False
                        View_map.count+=1
                elif View_map.count == self._row:
                    if j ==  '>' or j ==  '<' or j ==  '^' or j ==  'v':
                        self._view_assest_r(j, st.GREEN)

                    elif j == '*' or j=='#':
                        self._view_assest_r(j, st.RED)
                        
                    elif j == 'H':
                        self._view_assest_r(j, st.YELLOW)

                    else:
                        print(f'| {j} |', end='')
                        View_map.count = 1

            print('')
        # Print que crea la linea inferior del mapa 
        self._separator_line()



    def _number_up(self):
        print('  ', end='')
        for i in range(self._row):
            if i+1 >= 10:
                print(f'  {st.BLUE}{i+1}{st.RESET}', end='')
            else:
                print(f'  {st.BLUE}{i+1}{st.RESET} ', end='')
        print('')

    def _number_left(self, view_number):
        if view_number:
            if View_map.position >= 10:
                print(f'{st.BLUE}{View_map.position}{st.RESET}', end='')
            else:
                print(f'{st.BLUE}{View_map.position}{st.RESET} ', end='')
            View_map.position+=1

    def _view_assest(self, j, color):
        print(f'| {color}{j}{st.RESET} ', end='')
        View_map.count+=1

    def _view_assest_r(self, j, color):
        print(f'| {color}{j}{st.RESET} |', end='')
        View_map.count = 1

    def _separator_line(self):
        print('  ', end='')
        print(''.center((self._row*4)+1,'-'))