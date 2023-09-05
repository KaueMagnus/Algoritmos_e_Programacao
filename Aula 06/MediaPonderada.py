'''Calcular a media ponderada de três notas: 2, 3, 5'''

ponderada1 = 2
ponderada2 = 3
ponderada3 = 5

nota1 = float(input("Insira sua nota1: "))
nota2 = float(input("Insira sua nota2: "))
nota3 = float(input("Insira sua nota3: "))


mediaponderada = (float((ponderada1*nota1) + (ponderada2*nota2) + (ponderada3*nota3)) / (ponderada1+ponderada2+ponderada3))

print(f"A media ponderada é {mediaponderada:.2f}")