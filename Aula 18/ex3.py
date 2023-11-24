'''Crie uma função que determine se um número é par ou ímpar e retorne uma mensagem indicando o resultado.'''

def verificaPar(numero):
    par = numero % 2
    if par == 0:
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é ímpar!")
     

numero = int(input("Digite um numero: "))

verificaPar(numero)