'''Escreva um programa que leia um número e verifique se ele é positivo ou negativo. 
Se for positivo, exiba a mensagem "O número é positivo". 
Caso contrário, exiba "O número é negativo". O Programa encerra ao digitar 0. 
Ao fim deve exibir a quantidade dos numero pares e a soma de números impares.'''

soma_impares = 0
quant_pares = 0
while True:
    numero = int(input("Digite um numero: "))

    if numero == 0:
        break

    if numero > 0:
        print("O número é positivo")
        
    else:
        print("O número é negativo")
    
    if numero % 2 == 0:
        quant_pares += 1
    
    else:
        soma_impares += numero        

print(f"Quantidade de numeros pares: {quant_pares}")
print(f"Soma de numeros impares: {soma_impares}")        
        