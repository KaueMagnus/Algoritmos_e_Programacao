'''Solicite ao usuário seu peso em quilogramas e altura em metros.
Calcule o IMC. Mostre o IMC calculado.
'''
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (metros): "))

imc = peso / (altura * altura)

print(f"Seu IMC é {imc:.1f}")
