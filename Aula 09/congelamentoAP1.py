'''Com as mudanças climáticas, uma cidade está experimentando temperaturas extremas. O departamento de meteorologia quer alertar os cidadãos quando a temperatura se aproxima do ponto de congelamento.
Entrada:
O programa deve solicitar ao usuário a temperatura atual em graus Celsius.
Saída: 
O programa deve informar se está "Seguro", "Próximo ao ponto de congelamento" ou "Abaixo do ponto de congelamento".
* Seguro: Acima de 5°C
* Próximo ao ponto de congelamento: Entre 0°C e 5°C
* Abaixo do ponto de congelamento: Menos de 0°C
'''

tempAtual = float(input("Qual a temperatura em Celsius: "))

if tempAtual > 5:
    print("A temperatura está segura.")
elif tempAtual >= 0 and tempAtual <=5:
    print("A temperatura está próxima ao ponto de congelamento.")
elif tempAtual < 0:
    print("A temperatura está abaixo do ponto de congelamento.")        