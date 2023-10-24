'''Escreva um programa que leia o valor de um produto e calcule o valor com desconto de 10%. 
Se o valor do produto for maior que R$ 50,00, aplique um desconto adicional de 5%.
Exiba o valor final com desconto.'''

valor_produto = float(input("Digite o valor do produto: "))

desconto_10 = valor_produto * 0.10

if valor_produto > 50:
    desconto_5 = valor_produto * 0.05
    valor_desconto = valor_produto - (desconto_10 + desconto_5)
    
else:
    valor_desconto = valor_produto - desconto_10
    

print(f"O valor com desconto é: R${valor_desconto:.2f}")        