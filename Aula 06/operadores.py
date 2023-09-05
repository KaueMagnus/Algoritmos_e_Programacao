## Faça um programa que some dois numeros, se for maior que 10 mostre "Valor Maior que 10"
## Se for menor mostre "Valor menor que dez"

numX = int(input("Digite um valor para X: "))
numY = int(input("Digite um valor para Y: "))

soma = numX + numY

if soma > 10: 
    print(f"Valor maior que dez")

elif soma == 10:
    print("Valor igual a dez")

else: 
    print(f"Valor menor que dez")
