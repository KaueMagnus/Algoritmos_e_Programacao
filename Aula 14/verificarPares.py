'''Escreva um programa que leia um número inteiro e verifique se ele é par ou ímpar. 
Se for par, exiba a mensagem "O número é par".
Caso contrário, exiba "O número é ímpar". O Programa encerra ao digitar 0.
Ao fim deve exibir a soma dos numero pares e a quantidade de numeros impares'''

soma_pares = 0
quant_impares = 0

while True:
    numero = int(input("Digite um numero inteiro: "))

    if numero == 0:
        break
    
    if numero % 2 == 0:
        print("O numero é par")
        soma_pares += numero
    
    else:
        print("O numero é impar")    
        quant_impares += 1

print(f"Soma dos pares: {soma_pares}")        
print(f"Quantidade de impares: {quant_impares}")
    