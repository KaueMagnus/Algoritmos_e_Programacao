'''Solicite ao usuário a distância percorrida e a quantidade de combustível usado. 
Calcule o consumo médio usando Consumo = Distância / Combustível. Mostre o consumo em km/l.'''

distancia = float(input("Coloque a distancia percorrida"))
combustivel = float(input("Coloque o combustível"))
consumo = distancia / combustivel
print (f"O consumo médio é de: {consumo}Km/l")