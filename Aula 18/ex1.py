''' Crie uma função que realize operações de adição, subtração, multiplicação e divisão com dois números fornecidos como entrada e retorne o resultado.
'''

def soma (num1, num2):
    result = num1 + num2
    return result

def sub (num1, num2):
    result = num1 - num2
    return result

def mult (num1, num2):
    result = num1 * num2
    return result

def divisao (num1, num2):
    result = num1 / num2
    return result
   
        


print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("O que deseja fazer? "))

match opcao:
    case 1:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        resultado = soma(num1, num2)
        print(f"Resultado: {resultado:.2f}")

    case 2:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        resultado = sub(num1, num2)
        print(f"Resultado: {resultado:.2f}")

    case 3:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        resultado = mult(num1, num2)
        print(f"Resultado: {resultado:.2f}")

    case 4:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        if num1 != 0 and num2 != 0:
            resultado = divisao(num1, num2)
            print(f"{resultado}")
        else:
            print("Impossivel dividir com 0 na conta!")    
        