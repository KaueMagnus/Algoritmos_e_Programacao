'''Crie um algoritmo que, dada uma lista de números fornecida pelo usuário, encontre e imprima o maior numero da lista.'''


lista = []
tamanho_lista = int(input("Quantos números adicionar na lista? "))

for i in range(tamanho_lista):
    lista.append(int(input("Insira um numero na lista: ")))
    

if lista:
    maior = lista[0]
    
    for numeros in lista:
        if numeros > maior:
            maior =  numeros
            
    print(f"O maior númeor da lista é: {maior}")
    
else:
    print("Lista vazia")            
    
        