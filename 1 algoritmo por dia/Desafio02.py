'''solte a criatividade e crie um algoritmo que, 
ao inserir seu peso e altura, te apresente o resultado do seu IMC.'''

peso = float(input("Insira o seu peso (kg): "))
altura = float(input("Insira a sua altura (m): "))

imc = float( peso / (altura * altura))
nivel = str

if imc < 18.5:
    nivel = "Magreza"

elif imc >= 18.5 and imc <= 24.9:
    nivel = "Normal"

elif imc >= 25 and imc <= 29.9:
    nivel = "Sobrepeso"

elif imc >= 30 and imc <= 34.9:
    nivel = "Obesidade grau I"

elif imc >= 35 and imc <= 39.9:
    nivel = "Obesidade grau II"

elif imc >= 40:
    nivel = "Obesidade grau III"
    
else:
    print("Erro")
    
print(f"\nO seu IMC é {imc:.1f}\nClassificação: {nivel}")   
                            


