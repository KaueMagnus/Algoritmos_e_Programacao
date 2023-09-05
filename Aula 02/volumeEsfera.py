'''Volume de uma Esfera
   Peça ao usuário o raio de uma esfera. 
   Calcule o volume. Apresente o volume calculado.
'''


raio = float(input("Digite o raio da esfera: "))

volume = ((4/3) * 3.14 * (raio * raio * raio))

print(f"O volume da esfera é: {volume:.2f}")