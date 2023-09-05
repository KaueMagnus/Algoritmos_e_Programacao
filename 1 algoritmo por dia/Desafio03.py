'''Sextou! Galera, dizem que devemos calcular numa festa o chopp para uma festa da seguinte forma.
2 litros pra cada homem . 1.5 litros pra cada mulher.
Me ajuda aí um algoritmo pra calcular quantos litros de chopp dão necessários pra um happy hour!'''

quantHomens = int(input("Insira a quantidade de homens que irão na festa: "))
quantMulheres = int(input("Insira a quantidade de mulheres que irão na festa: "))

choppHomens = float(2 * quantHomens)
choppMulheres = float(1.5 * quantMulheres)

choppTotal = float(choppHomens + choppMulheres)

print(f"A quantidade de chopp necessária para a festa é de {choppTotal} Litros")