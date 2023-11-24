'''Crie um programa que permita ao usuário calcular a média de um conjunto de notas. 
O programa deve oferecer as seguintes opções no menu:
     1. Adicionar notas à lista.
     2. Calcular a média das notas.
     3. Exibir a média calculada.
'''

notas = []
opcao = 0
soma = 0
quant_notas = 0
nota = 0

while opcao != 8:

    print("1 - Adicionar nota à lista")
    print("2 - Calcular a média das notas")
    print("3 - Exibir a média calculada")
    print("8 - Encerrar programa")

    opcao = int(input("Digite a ação a ser feita: "))

    if opcao == 1:
        nota = (float(input("Digite o valor da nota: ")))
        notas.append(nota)
        quant_notas += 1
        soma += nota

    elif opcao == 2:
        if quant_notas > 0:
            media = float(soma / quant_notas)
            print("Calculo de média realizado!\n")
        
        else:
            print("Não há notas para calcular a média.\n")

    elif opcao == 3:
        print(f"A média das notas é: {media:.1f}")
    
    elif opcao == 8:
        break

print("Encerrando programa...")
        
            
