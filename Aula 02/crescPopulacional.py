'''Peça ao usuário a população atual e a taxa de crescimento anual de duas cidades.
Calcule a população de cada cidade após um ano e mostre os novos valores.'''

cidade1 = int(input("Digite a população atual da primeira cidade: "))
crescimento1 = float(input("Digite a taxa de crescimento anual da primeira cidade (%): ")) / 100

cidade2 = int(input("Digite a população atual da segunda cidade: "))
crescimento2 = float(input("Digite a taxa de crescimento anual da segunda cidade (%): ")) / 100

populacaocidade1 = cidade1 * (1 + crescimento1)
populacaocidade2 = cidade2 * (1 + crescimento2)

print("Nova população da primeira cidade após um ano:", int(populacaocidade1))
print("Nova população da segunda cidade após um ano:", int(populacaocidade2))