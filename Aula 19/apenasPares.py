'''Desenvolva um algoritmo que percorra uma lista de números e imprima apenas aqueles que são pares.'''

lista = []
tamanho_lista = int(input("Qual o tamanho da lista: "))

for i in range(tamanho_lista):
    lista.append(int(input("Digite um numero: ")))


if lista:
    
    print("Numeros pares:")
    for numeros in lista:
        if numeros % 2 == 0:
            print(numeros)
    
else:
    print(f"Lista vazia")               