'''Peça ao usuário um valor principal, a taxa de juros e o tempo em anos.
Calcule o juro simples. Mostre o valor de juros.
'''

valor = float(input("Digite o valor (R$): "))
taxaJuros = float(input("Digite a taxa de juros (%): "))
tempo = float(input("Digite o tempo em anos: "))

taxaJuros_decimal = taxaJuros / 100;

juroSimples = valor * taxaJuros_decimal * tempo

print(f"O valor do juro simples é: {juroSimples}")