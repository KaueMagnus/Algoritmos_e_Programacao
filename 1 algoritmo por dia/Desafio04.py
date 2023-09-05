'''Sabendo que o Sky come duas vezes no dia 180 gramas de ração.
Que o preço medio do saco de ração de 10kg é de 200 reais ( come melhor que eu esse jaguara)
Faça um algoritmo que mostre quanto vou gastar de dinheiro em um ano.'''

racaoMes = float((180 * 2) * 30)    #Aqui eu multiplico o 180 pela quant de refeições, que multiplica pelo numero de dias no mês

racaoKG = float(racaoMes / 1000)    #Convertendo o consumo do mes para KG

valorKG = 200 / 10                  #Calculando o preço de cada KG do saco de ração  

valorMensal = racaoKG * valorKG     #Multiplicando o consumo mensal em KG com o valor de cada KG      

valorAno = float(valorMensal * 12)  #Calculando o valor mensal multiplicado por 12 meses (1 ano)

print(f"O valor gasto em ração durante 1 ano é de {valorAno:.2f}")