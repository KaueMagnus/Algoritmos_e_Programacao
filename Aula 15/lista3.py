'''Construa um programa que permita ao usuário criar uma lista de números e, em seguida, 
criar uma nova lista contendo apenas os números pares da lista original. 
O programa deve oferecer as seguintes opções no menu:
     1. Adicionar números à lista.
     2. Criar uma nova lista apenas com os números pares.
     3. Exibir a lista com números pares.
'''

lista = []
lista_pares = []

while True:
    print("1- Adicionar número a lista.")
    print("2- Criar nova lista com os numeros pares.")
    print("3- Exibir a lista com os numeros pares.")
    print("9- Encerrar programa.")
    
    opcao = int(input("Digite o que deseja realizar: "))1
