'''Verificar se um numero é par ou impar'''

numX = int(input("Digite um numero inteiro: "))

resto = numX % 2

if resto == 0:
    print("O valor é par!")

else:
    print("O valor é impar!")    