'''Elabore um programa que leia dois números e some 100 ao maior valor e apresente o resultado.'''

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

if num1 > num2:
    print(f"O maior numero é o num1: {num1 + 100}")
else:
    print(f"O maior numero é o num2: {num2 + 100}")    