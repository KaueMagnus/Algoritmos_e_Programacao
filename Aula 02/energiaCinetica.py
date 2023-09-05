'''Energia Cinética
   Peça ao usuário a massa de um objeto em quilogramas e sua velocidade em metros por segundo.
   Calcule a energia cinética. Apresente o valor
'''

massa = float(input("Digite a massa (peso) do objeto em kg: "))
speed = float(input("Digite a velocidade do objeto (m/s): "))

energiaC = float((massa * (speed * speed)) / 2)

print(f"A energia cinetica do objeto é de {energiaC:.2f} Joules")