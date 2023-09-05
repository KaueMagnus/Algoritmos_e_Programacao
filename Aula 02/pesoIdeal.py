'''Solicite a altura do usuário.
Calcule o peso ideal como PesoIdeal = 52 + (0.75 * (altura - 152.4). Mostre o peso ideal calculado.'''

altura = float(input("Coloque a sua altura (cm): "))
pesoideal = 52 + (0.75 * (altura - 152.4))
print (f"O seu peso ideal é: {pesoideal:.1f}kg")