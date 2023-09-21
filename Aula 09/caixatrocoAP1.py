'''Para treinar seus conhecimentos em Python, você decide criar um programa simples de caixa que ajude a calcular o troco dado ao cliente.
Entrada: 
O programa deve perguntar o valor total da compra e o valor entregue pelo cliente para pagar.
Saída: 
O programa deve informar o valor do troco que o cliente deve receber.
'''

totalCompra = float(input("Qual o valor total da compra? "))
valorEntregue = float(input("Qual o valor pago pelo cliente? "))

troco = valorEntregue - totalCompra

print(f"O troco será de R${troco:.2f}")


