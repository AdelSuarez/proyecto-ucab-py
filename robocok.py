map = []

y = int(input('introduce la cantidad de columnas >> '))
x = int(input('Introduce la cantidad de filas >> '))


if y > x:
    for i in range(x):
        map.append([])
        for j in range(y):
            map[i].append(0)

    print(f' C: {y} | F: {x} '.center((y*4)+1,'-'))
        
    count = 1
    for i in range(len(map)):
        print(''.center((y*4)+1,'-'))
        for j in map[i]:
            if count < y:
                print(f'| {j} ', end='')
                count+=1
            elif count == y:
                print(f'| {j} |', end='')
                count = 1

        print('')
    print(''.center((y*4)+1,'-'))
else:
    print('Las columnas no puedes ser menores a las filas')

        


