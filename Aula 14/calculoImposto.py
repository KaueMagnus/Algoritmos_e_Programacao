'''Escreva um programa que leia o salário de um funcionário e
calcule o valor do imposto a ser pago, considerando as seguintes faixas salariais:
até R$ 1.000,00, isento de imposto; de R$ 1.000,00 a R$ 2.000,00, 10% de imposto; acima de R$ 2.000,00, 20% de imposto. 
O Programa encerra ao calular 20 funcionários ou se o salario for 0'''

quant_funcionarios = 0

while quant_funcionarios < 3:
    salario = float(input("Digite o salario do funcionario: "))

    if salario == 0:
        break
    
    if salario < 1000:
        imposto = 0 
    
    elif salario <= 2000:
        imposto = 0.10 * salario
    
    else:
        imposto = 0.20 * salario    
    
    salario_liquido = salario - imposto
    
    print(f"Salário: R${salario:.2f}")               
    print(f"Imposto: R${imposto:.2f}")
    print(f"Salário líquido: R${salario_liquido:.2f}")
    
    quant_funcionarios += 1
    
print("Encerrando programa...")    

    