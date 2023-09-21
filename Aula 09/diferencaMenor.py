'''Faça um programa para ler dois valores numéricos e apresentar a diferença do maior pelo menor. '''

num1 = int(input("Insira um numero: "))
num2 = int(input("Insira um numero: "))

if num1 > num2:
    print(f"A diferença de {num1} e {num2} é {num1 - num2}")

else:
    print(f"A diferença de {num2} e {num1} é {num2 - num1}")