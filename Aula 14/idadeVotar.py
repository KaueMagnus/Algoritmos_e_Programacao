'''Escreva um programa que peça a idade do usuário e verifique se ele pode votar ou não.
Se a idade for igual ou superior a 16 anos, exiba a mensagem "Você pode votar".
Caso contrário, exiba "Você ainda não pode votar".'''

idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Você pode votar")

else: 
    print("Você ainda não pode votar")