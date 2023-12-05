'''Descrição: Escreva uma função que recebe dois parâmetros, uma lista com dez números inteiros e um número inteiro.
A função deve verificar quantas vezes este número aparece na lista.
Por fim, a função deve retornar esta contagem.
Por exemplo, se a lista for [1, 3, 7, 8, 7, 5, 6, 7, 9, 0] e o número a ser buscado for 7, o algoritmo deve imprimir 3,
pois o número 7 aparece três vezes na lista. 
Objetivo: Este exercício testa a capacidade dos alunos de combinar laços de repetição com operações de lista para realizar buscas e contagens, habilidades importantes em programação.'''

def conta_ocorrencias(numeros, num_buscador):
    contador_num = 0
    for num in numeros:
        if num_buscador == num:
            contador_num += 1

    print(f"O número {num_buscador} aparece {contador_num} vezes na lista.")
    return contador_num

lista = []

tamanho_lista = int(input("Qual o tamanho da lista? "))

for _ in range(tamanho_lista):
    numero = int(input("Insira um numero na lista: "))
    lista.append(numero)

num_buscador = int(input("Qual numero deseja buscar? "))

conta_ocorrencias(lista, num_buscador)



                