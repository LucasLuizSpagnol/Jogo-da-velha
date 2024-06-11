
print('JOGO DA VELHA')

matriz = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]
nome1 = input('jogador 1: ')
nome2 = input('Jogador 2: ')
print('')
i = 4
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('')
while i != 0:
    print(f'{nome1}, faça sua jogada: ')
    x, y = map(int, input('Linha e coluna: ').split())
    matriz[x][y] = 'x'
    i-=1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print('')
    if matriz[0][0] == 'x' and matriz[1][0] == 'x' and matriz[2][0] == 'x':
        print(f'{nome1} ganhou!')
        break
    elif matriz[0][1] == 'x' and matriz[1][1] == 'x' and matriz[2][1] == 'x':
        print(f'{nome1} ganhou!')
        break
    elif matriz[0][2] == 'x' and matriz[1][2] == 'x' and matriz[2][2] == 'x':
        print(f'{nome1} ganhou!')
        break
    elif matriz[0][0] == 'x' and matriz[0][1] == 'x' and matriz[0][2] == 'x':
        print(f'{nome1} ganhou!')
        break
    elif matriz[1][0] == 'x' and matriz[1][1] == 'x' and matriz[1][2] == 'x':
        print(f'{nome1} ganhou!')
        break
    elif matriz[2][0] == 'x' and matriz[2][1] == 'x' and matriz[2][2] == 'x':
        print(f'{nome1} ganhou!')
        break
    elif matriz[0][0] == 'x' and matriz[1][1] == 'x' and matriz[2][2] == 'x':
        print(f'{nome1} ganhou!')
        break
    elif matriz[0][2] == 'x' and matriz[1][1] == 'x' and matriz[2][0] == 'x':
        print(f'{nome1} ganhou!')
        break
    print(f'{nome2}, faça sua jogada: ')
    x, y = map(int, input('Linha e coluna: ').split())
    matriz[x][y] = 'O'
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])

    if matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O':
        print(f'{nome2} ganhou!')
        break
    elif matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O':
        print(f'{nome2} ganhou!')
        break
    elif matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O':
        print(f'{nome2} ganhou!')
        break
    elif matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O':
        print(f'{nome2} ganhou!')
        break
    elif matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O':
        print(f'{nome2} ganhou!')
        break
    elif matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O':
        print(f'{nome2} ganhou!')
        break
    elif matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O':
        print(f'{nome2} ganhou!')
        break
    elif matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O':
        print(f'{nome2} ganhou!')
        break
    else:
        print('')
    if i == 0:
        print(f'{nome1}, faça sua jogada: ')
        x, y = map(int, input('Linha e coluna: ').split())
        matriz[x][y] = 'x'
        i-=1
        print(matriz[0])
        print(matriz[1])
        print(matriz[2])
        print('')

        if matriz[0][0] == 'x' and matriz[1][0] == 'x' and matriz[2][0] == 'x':
            print(f'{nome1} ganhou!')
            break
        elif matriz[0][1] == 'x' and matriz[1][1] == 'x' and matriz[2][1] == 'x':
            print(f'{nome1} ganhou!')
            break
        elif matriz[0][2] == 'x' and matriz[1][2] == 'x' and matriz[2][2] == 'x':
            print(f'{nome1} ganhou!')
            break
        elif matriz[0][0] == 'x' and matriz[0][1] == 'x' and matriz[0][2] == 'x':
            print(f'{nome1} ganhou!')
            break
        elif matriz[1][0] == 'x' and matriz[1][1] == 'x' and matriz[1][2] == 'x':
            print(f'{nome1} ganhou!')
            break
        elif matriz[2][0] == 'x' and matriz[2][1] == 'x' and matriz[2][2] == 'x':
            print(f'{nome1} ganhou!')
            break
        elif matriz[0][0] == 'x' and matriz[1][1] == 'x' and matriz[2][2] == 'x':
            print(f'{nome1} ganhou!')
            break
        elif matriz[0][2] == 'x' and matriz[1][1] == 'x' and matriz[2][0] == 'x':
            print(f'{nome1} ganhou!')
            break
        else:
            print('Empate!')
            break

