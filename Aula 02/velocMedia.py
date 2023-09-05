'''Velocidade Média
   Peça ao usuário o espaço percorrido em metros e o tempo gasto em segundos. 
   Calcule a velocidade média. Apresente o resultado.
'''
distancia = float(input("Quantos metros foram percorridos?: "))
tempo = float(input("Quanto tempo levou? (em segundos): "))

media = float(distancia/tempo)
mediaKm = float(media * 3.6)

print(f"Velocidade media: {media:.1f} m/s\nVelocidade media: {mediaKm:.1f} km/h")