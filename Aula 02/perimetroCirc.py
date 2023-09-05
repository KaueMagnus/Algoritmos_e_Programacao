'''Perímetro de um Círculo
   Solicite ao usuário o raio de um círculo.
   Calcule o perímetro (ou circunferência) usando Perímetro = 2 π r. Mostre o perímetro calculado.
'''

raio = float(input("Digite o valor do raio do circulo:"))
pi = 3.14

perimetro = float(2 * pi * raio)

print(f"O circulo com um raio de {raio} tem um perimetro  igual a {perimetro}")