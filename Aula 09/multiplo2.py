'''Elabore um programa que lê dois valores e escreve cada um com a mensagem: “É múltiplo de 2” ou “Não é múltiplo de dois".'''

num1 = float(input("Digite o numero 1: "))
num2 = float(input("Digite o numero 2: "))

num1Mult = num1 % 2
num2Mult = num2 % 2

if num1Mult == 0:
    print(f"{num1} é multiplo de dois")
else:
    print(f"{num1} não é multiplo de dois")   

if num2Mult == 0:
    print(f"{num2} é multiplo de dois")
else:
    print(f"{num2} não é multiplo de dois")         