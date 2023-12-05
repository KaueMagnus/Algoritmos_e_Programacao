'''Escreva um algoritmo que remova um item especifico de uma lista, baseado no valor fornecido pelo usuario, e depois imprima a lista atualizada.'''

lista = []
tamanho_lista = int(input("Digite o tamanho da lista: "))

for i in range(tamanho_lista):
    lista.append(int(input("Digite um numero: ")))

if lista:
    valor_remover = int(input("Valor a ser removido: "))
    
    if valor_remover in lista:
        lista.remove(valor_remover)
        
        print(f"Lista atualizada:", lista)
    
    else:
        print(f"Não existe o valor {valor_remover} na lista.")
else:
    print("Lista vazia")            
    