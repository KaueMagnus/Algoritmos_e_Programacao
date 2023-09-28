'''Crie um programa que peça ao usuário para digitar um número e, em seguida,
exiba a tabuada desse número de 1 a 10 usando um loop while.'''

x = int(input("Digite um numero inteiro positivo: "))
i = int(1)

while i <= 10:
    mult = int(x * i)
    print(f"{x} x {i} = {mult}")
    i += 1    
    