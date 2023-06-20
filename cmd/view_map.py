import style.style as st

class View_map:
    
    def __init__(self,column, map_game) -> None:
        self._column = column
        self.map_game = map_game


    def view(self):
        position = 1

        self._number_up()
        
        for row in range(len(self.map_game)):
            
            view_number = True
            count = 1
            # Print que crea la linea superior del mapa 
            self._separator_line()
            

            # Ciclos que imprime el mapa sin los [] de las listas
            for column in self.map_game[row]:

                # TODO: optimizar el codigo
                if view_number:
                    if position >= 10:
                        print(f'{st.BLUE}{position}{st.RESET}', end='')
                    else:
                        print(f'{st.BLUE}{position}{st.RESET} ', end='')
                    position+=1

                if count < self._column:
                    if column ==  '>' or column ==  '<' or column ==  '^' or column ==  'v': 
                        print(f'| {st.GREEN}{column}{st.RESET} ', end='')
                        view_number=False
                        count+=1

                    elif column == '*' or column=='#':
                        print(f'| {st.RED}{column}{st.RESET} ', end='')
                        view_number=False
                        count+=1

                    elif column == 'H':
                        print(f'| {st.YELLOW}{column}{st.RESET} ', end='')
                        view_number=False
                        count+=1

                    else:
                        print(f'| {column} ', end='')
                        view_number=False
                        count+=1
                elif count == self._column:
                    if column ==  '>' or column ==  '<' or column ==  '^' or column ==  'v':
                        print(f'| {st.GREEN}{column}{st.RESET} |', end='')
                        count+=1

                    elif column == '*' or column=='#':
                        print(f'| {st.RED}{column}{st.RESET} |', end='')
                        count+=1
                        
                    elif column == 'H':
                        print(f'| {st.YELLOW}{column}{st.RESET} |', end='')
                        count+=1

                    else:
                        print(f'| {column} |', end='')
                        count = 1

            print('')
        # Print que crea la linea inferior del mapa 
        self._separator_line()



    def _number_up(self):
        print('  ', end='')
        for i in range(self._column):
            if i+1 >= 10:
                print(f'  {st.BLUE}{i+1}{st.RESET}', end='')
            else:
                print(f'  {st.BLUE}{i+1}{st.RESET} ', end='')
        print('')

    def _separator_line(self):
        print('  ', end='')
        print(''.center((self._column*4)+1,'-'))