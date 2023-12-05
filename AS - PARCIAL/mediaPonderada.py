'''Desenvolva uma função chamada media_ponderada que receba duas listas: uma lista de notas e uma lista de pesos correspondentes a essas notas.
A função deve calcular e retornar a média ponderada das notas. 
Por exemplo, se as notas forem [8, 5, 7] e os pesos [2, 3, 5], a média ponderada será (8*2 + 5*3 + 7*5) / (2 + 3 + 5). 
Se as listas estiverem vazias ou de tamanhos diferentes, a função deve retornar None.

Objetivo: Este exercício pretende testar a habilidade dos alunos em manipular listas e aplicar conceitos matemáticos básicos, como a média ponderada. 
Ele também ensina a importância de verificar a consistência dos dados (por exemplo, garantindo que as listas tenham o mesmo tamanho).'''

def media_ponderada(notas, pesos):
    if not notas or not pesos or len(notas) != len(pesos):
        return None

    soma_produtos = sum(nota * peso for nota, peso in zip(notas, pesos))
    soma_pesos = sum(pesos)

    if soma_pesos == 0:
        return None

    return soma_produtos / soma_pesos

notas = []
pesos = []

tamanho_lista = int(input("Quantas notas você deseja inserir? "))

for _ in range(tamanho_lista):
    nota = float(input("Insira uma nota: "))
    peso = float(input("Insira o peso correspondente à nota: "))

    notas.append(nota)
    pesos.append(peso)

resultado = media_ponderada(notas, pesos)

if resultado is not None:
    print(f"A média ponderada é: {resultado:.2f}")
else:
    print("As listas estão vazias ou tem tamanhos diferentes.")