'''Escreva um programa que calcule a soma de todos os números pares de 1 a 100 usando um loop while.
'''

total = 0
contagem = 2
while contagem <= 100:
    total += contagem
    contagem += 2

print(f"A soma dos numeros pares de 1 a 100 é {total}")
    