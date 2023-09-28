'''Crie um programa que gere a tabuada de multiplicação de um número inserido pelo usuário usando um loop while.'''

x = int(input("Digite um numero inteiro positivo: "))
i = int(1)

while i <= 10:
    mult = int(x * i)
    print(f"{x} x {i} = {mult}")
    i += 1   