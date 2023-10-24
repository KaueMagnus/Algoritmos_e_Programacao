'''Escreva um programa que leia três notas e calcule a média do aluno. 
Se a média for maior ou igual a 7, exiba a mensagem "Aprovado".
Caso contrário, exiba "Reprovado". 
O programa encerra ao efetuar 10 leituras ou até o usuário digitar 3 notas zero.
'''

notas_contador = 0

while notas_contador < 10:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    if nota1 == 0 and nota2 == 0 and nota3 == 0:
        print("Zerou tres notas.")
        break
    
    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 7:
        print(f"Média: {media:.1f} ---- Aprovado")
    else:
        print(f"Média: {media:.1f} ---- Reprovado")
        
    notas_contador += 1    
        
print("Encerrando programa...")            