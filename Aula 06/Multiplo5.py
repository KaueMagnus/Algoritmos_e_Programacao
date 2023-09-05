'''Verificar se um numero é multiplo de 5'''

num1 = int(input("Digite um numero inteiro: "))

multiplo = num1 % 5

if multiplo == 0:
    print("O valor é multiplo de 5!")

else:
    print("O valor não é multiplo de 5!")    