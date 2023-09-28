'''Soma de Números Ímpares: Calcule a soma de todos os números ímpares de 1 a 100 usando um loop while.
'''

total = 0
contagem = 1
while contagem <= 100:
    total += contagem
    contagem += 2

print(f"A soma dos numeros impares de 1 a 100 é {total}")