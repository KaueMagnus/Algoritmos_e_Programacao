'''Calcular e exibir o maior de quatro números.'''

num1 = int(input("Digite o numero1: "))
num2 = int(input("Digite o numero2: "))
num3 = int(input("Digite o numero3: "))
num4 = int(input("Digite o numero4: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"O maior numero é {num1}")

elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"O maior numero é {num2}")
        
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"O maior numero é {num3}") 
       
elif num4 > num1 and num4 > num3 and num4 > num2:
    print(f"O maior numero é {num4}")    