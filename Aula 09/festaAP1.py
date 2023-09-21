'''Você está planejando uma festa de aniversário e quer garantir que não falte bebida. Decide criar um programa que calcule a quantidade de bebida necessária.
Entrada:
O programa deve solicitar o número de convidados.
Saída:
O programa deve informar a quantidade total de bebida (em litros) que você precisa comprar.
Nota: 
Estime que cada convidado consuma 500ml de bebida.
'''

convidados = int(input("Quantos convidados irão a festa? "))

bebida = float((convidados * 500) / 1000)

print(f"Será necessário comprar {bebida} litros de bebida para festa")