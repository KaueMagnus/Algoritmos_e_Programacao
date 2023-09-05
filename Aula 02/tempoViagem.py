'''Solicite ao usuário a distância de uma viagem em km e a velocidade média esperada em km/h.
Calcule o tempo da viagem como Tempo = Distância / Velocidade. Mostre o tempo previsto'''

distancia = float(input("Coloque a distância em KM"))
speed = float(input("Coloque a velocidade"))
tempo = distancia / speed
print (f"O tempo previsto é de :{tempo} horas")