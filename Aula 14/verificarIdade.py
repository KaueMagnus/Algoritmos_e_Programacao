'''Escreva um programa que peça a idade do usuário e verifique se 
ele é maior de idade ou não. Se for maior de idade, exiba a mensagem "Você é maior de idade"
Caso contrário, exiba "Você é menor de idade". 
O Programa deve perguntar "Deseja efetuar nova validação (S/N)" O programa encerra ao digitar N'''

while True:
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
        
    resetar = input("Deseja efetuar nova validação? (S/N) ").upper().strip()   
    
    if resetar == "N":
        break
    
print("Encerrando programa...")         