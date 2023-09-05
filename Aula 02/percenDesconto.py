'''Peça ao usuário o preço original de um produto e um desconto em porcentagem.
Calcule o valor com desconto usando ValorComDesconto = ValorOriginal - (ValorOriginal * Desconto / 100).
Mostre o valor após o desconto.
'''
n1=float (input("Insira o valor em dolares"))
des=float (input("insira o desconto"))
VO = n1 - (n1 * des / 100)
print (f"O valor com desconto fica: {VO} reais")
