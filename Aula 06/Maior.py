'''Calcular e exibir o maior de três números.'''

num1 = float(input("Digite o valor 1: "))
num2 = float(input("Digite o valor 2: "))
num3 = float(input("Digite o valor 3: "))

if num1 > num2 and num1 > num3:
    print(f"Num1 é o maior valor com {num1}")

elif num2 > num3 and num2 > num1:
    print(f"Num2 é o maior valor com {num2}")

elif num3 > num2 and num3 > num1:
    print(f"Num3 é o maior valor com {num3}")



