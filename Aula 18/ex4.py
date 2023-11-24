'''Escreva uma função que converta uma temperatura em graus Celsius para graus Fahrenheit.
'''

def converterTemp(temp):
    fahr = float((temp * (9/5)) + 32)
    print(f"Temperatura em Celsius: {temp:.1f}\nTemperatura em Fahrenheit: {fahr:.1f}")

temp = float(input("Digite a temperatura em Celsius: "))

converterTemp(temp)

