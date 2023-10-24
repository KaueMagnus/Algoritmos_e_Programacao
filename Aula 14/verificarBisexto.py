'''Escreva um programa que peça ao usuário um ano e verifique-se ele é bissexto ou não. 
Um ano é bissexto se for divisível por 4 e não for divisível por 100, exceto quando é divisível por 400. 
Se o ano for bissexto, exiba a mensagem "O ano é bissexto". 
Caso contrário, exiba "O ano não é bissexto". 
O Programa encerra ao digitar 3 anos consecutivos não bissextos.'''

anos_nao_bissextos_consecutivos = 0

while anos_nao_bissextos_consecutivos < 3:
    ano = int(input("Digite um ano (ou 0 para encerrar): "))
    
    if ano == 0:
        break

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("O ano é bissexto.")
        anos_nao_bissextos_consecutivos = 0  # Reseta o contador
    else:
        print("O ano não é bissexto.")
        anos_nao_bissextos_consecutivos += 1

print("Programa encerrado.")