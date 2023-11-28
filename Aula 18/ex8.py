'''Implemente uma função que calcule o fatorial de um número inteiro não negativo.
'''

def calcular_fatorial(numero):
    if numero < 0:
        print("Entrada inválida: O fatorial é definido apenas para números inteiros não negativos.")
        return -1
    
    resultado = 1
    while numero > 1:
        resultado *= numero
        numero -= 1
    
    return resultado

numero = int(input("Digite um número: "))
fatorial_resultado = calcular_fatorial(numero)
if fatorial_resultado != -1:
    print(f"O fatorial de {numero} é: {fatorial_resultado}")