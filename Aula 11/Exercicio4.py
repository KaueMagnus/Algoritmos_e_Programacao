'''Crie um programa que solicite ao usuário um número e, em seguida, conte e exiba a quantidade de dígitos desse número usando um loop while'''

numero = int(input("Digite um número inteiro: "))

contador = 0

if numero == 0:
    contador = 1

while numero != 0:
    numero //= 10  
    contador += 1   

print(f"O número tem {contador} dígitos.")