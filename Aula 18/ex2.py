'''Escreva uma função que calcule a média de uma lista de números.'''

def media(soma, x):
    for x in lista:
        x = 0
        x += x
        div = float(soma / limite)
    return div    

lista = []
x = 1

limite = int(input("Digite o tamanho da lista: "))


while x <= limite:
    lista.append(float(input(f"Digite o {x}º número da lista: ")))
    x += 1
    soma = sum(lista)

resultado = media(soma, x)
print(f"Média da lista com {limite} numeros: {resultado:.2f}")