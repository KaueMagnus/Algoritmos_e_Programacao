'''Faça um programa para ler dois números. Se os números forem iguais imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar a execução; caso contrário, imprimir o de maior valor.'''

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))

if num1 == num2:
    print("NÚMEROS IGUAIS")

elif num1 > num2:
    print(f"Maior valor é {num1}")

elif num2 > num1:
    print(f"Maior valor é {num2}")    