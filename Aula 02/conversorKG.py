'''Conversor de Massa
   Solicite ao usuário um peso em quilogramas. 
   Converta este valor para gramas. Mostre o resultado.
'''

pesoKG = float(input("Digite o seu peso (kg):"))
pesoG = float(pesoKG * 1000)

print(f"Seu peso em kilogramas: {pesoKG} kg\nSeu peso em gramas: {pesoG:,.2f} gramas")