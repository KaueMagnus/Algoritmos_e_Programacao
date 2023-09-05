'''Verificar se um número é divisível por 3 e 5 ao mesmo tempo.'''

numX = int(input("Digite o valor de numX: "))

divisivel3 = numX % 3
divisivel5 = numX % 5

if divisivel3 == 0 and divisivel5 == 0:
    print(f"O numero {numX} é divisivel por 3 e 5!")

else:
    print(f"O numero {numX} não é divisivel por 3 e 5!")
        