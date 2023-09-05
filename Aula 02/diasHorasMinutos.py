'''Solicite ao usuário uma quantidade em minutos. 
Converta essa quantidade para dias, horas e minutos, 
considerando que um dia tem 24 horas e uma hora tem 60 minutos.
Mostre o resultado da conversão.'''

minutos=float (input("Digite uma quantidade de minutos: "))
horas=round (minutos/60, 1)
dias=round (horas/24, 1)


print(f"Horas: {horas}")
print(f"Dias: {dias}")