lista = []
opcao = 0
while opcao != 9:
    print("\n=======GERENCIAR LISTA DE COMPRAS=======")
    print("\n1 - Adicionar item a lista")
    print("\n2 - Remover item da lista")
    print("\n3 - Exibir os itens da lista")
    print("\n9 - Sair")

    opcao = int(input("O que deseja fazer? "))

    if opcao == 1:
        lista.append(input("Qual item adicionar? "))

    elif opcao == 2:
        lista.remove(input("Qual item remover? "))    

    elif opcao == 3:
        print(f"=======Lista de compras=======")    
        for item in lista:
            print(f"{item}") 

    elif opcao == 9:
        break

