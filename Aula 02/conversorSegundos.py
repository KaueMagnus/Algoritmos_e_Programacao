'''Conversor de Segundos
   Solicite ao usuário um valor em segundos. 
   Converta esse valor para horas, minutos e segundos. Mostre o resultado.
'''
segundos = float(input("Insira um valor em segundos: "))
minutos = float(segundos / 60)
horas = float(minutos / 60)

print(f"Segundos: {segundos:.1f}\nMinutos: {minutos:.1f}\nHoras: {horas:.1f}")

