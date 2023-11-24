'''Crie uma função que verifique se uma palavra é um palíndromo
(ou seja, pode ser lida da mesma forma da esquerda para a direita e vice-versa).'''

def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")

if palindromo(palavra):
    print(f"{palavra} é um palíndromo")
else:
    print(f"{palavra} não é um palíndromo")    