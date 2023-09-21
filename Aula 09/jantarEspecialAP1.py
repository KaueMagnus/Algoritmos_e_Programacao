'''Para um jantar em família, além do espaguete, agora você também deseja servir um molho especial para pessoas veganas.
Entrada: 
O programa deve perguntar quantos membros da família vão participar do jantar e quantos deles são veganos.
Saída 
O programa deve informar a quantidade de espaguete (em gramas) e a quantidade de molho (em litros) que você precisa preparar.
* Espaguete: 100g por pessoa
* Molho: 0,5 litros para cada vegano
'''

convidados = int(input("Quantas pessoas participarão do jantar? "))
veganos = int(input("Quantos convidados são veganos? "))

espaguete = 100 * convidados
molho = (500 * veganos) / 1000

print(f"A quantidade de espaguete necessário para o jantar será de {espaguete} gramas")
print(f"A quantidade de molho para veganos será de {molho} litros.")