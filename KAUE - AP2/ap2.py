'''Seu programa deve ter um menu com as seguintes opções:

Adicionar Produto
Adicionar Produto em uma Posição Específica
Remover Produto
Listar Produtos
Sair

A opção 1 deve permitir que o usuário adicione um produto à lista.
A opção 2 deve permitir que o usuário adicione um produto em uma posição específica da lista.
A opção 3 deve permitir que o usuário remova um produto da lista.
A opção 4 deve listar todos os produtos na lista.
A opção 9 deve encerrar o programa.
'''
import os

opcao = 0
produtos = []
itens = 0

os.system("cls")
print("Bem-vindo ao Gerenciador de Produtos!\n")
while opcao != 9:
    print("\nMenu:")
    print("1. Adicionar Produto")
    print("2. Adicionar Produto em uma Posição Específica")
    print("3. Remover Produto")
    print("4. Listar Produtos")
    print("9. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    match opcao:
        case 1:
            nome = input("Digite o nome do produto: ")
            if nome in produtos:
                print(f"O produto {nome} já está na lista. Não é permitido adicionar produtos repetidos.")
                break

            else:
                produtos.append(nome)
            
            print(f"Produto '{nome}' adicionado com sucesso!")
    
        case 2:
            nome = input("Digite o nome do produto: ")
            if nome in produtos:
                print(f"O produto {nome} já está na lista. Não é permitido adicionar produtos repetidos.")
                break

            else:
                posicao = int(input(f"Em qual posição você deseja adicionar '{nome}'? (0 a {len(produtos)})"))
                produtos.insert(posicao, nome)
                print(f"Produto '{nome}' adicionado com sucesso!")        
        
        case 3:
            nome = input("Digite o nome do produto que deseja remover: ")
            produtos.remove(nome)
            print(f"Produto '{nome}' removido com sucesso!")
        
        case 4:
            if produtos:
                print("Lista de Produtos:")
                for i, produto in enumerate(produtos):
                    print(f"{i + 1}. {produto}")
            else:
                print("A lista de produtos está vazia.")
                
        case 9:
            print("Obrigado por usar o Gerenciador de Produtos! Até logo!")
            break
        
        case _:
            print("Opção Inválida, tente novamente!")        