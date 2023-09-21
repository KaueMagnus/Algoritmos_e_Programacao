'''Você faz parte da equipe de logística de uma missão espacial que está planejando uma viagem à Lua. Sua tarefa é determinar a quantidade de suprimentos e combustível necessários, considerando vários fatores.

1. `numAstronautas`: Número de astronautas na missão.
2. `diasMissao`: Duração total da missão em dias.
3. `consumoOxigenio`: Consumo diário médio de oxigênio por astronauta em litros.
4. `consumoAgua`: Consumo diário médio de água por astronauta em litros.
5. `consumoComida`: Consumo diário médio de comida por astronauta em quilogramas.
6. `pesoFoguete`: Peso do foguete vazio em quilogramas.
7. `eficienciaCombustivel`: Eficiência do combustível (quantos quilômetros por litro).
8. `distanciaLua`: Distância média da Terra à Lua em quilômetros (384.400 km).
9. `reservaEmergencia`: Porcentagem de suprimentos extras para emergências.
10. `capacidadeTanque`: Capacidade máxima do tanque de combustível em litros.

Fórmulas:

1. Suprimentos de oxigênio: `numAstronautas * diasMissao * consumoOxigenio * (1 + reservaEmergencia/100)`
2. Suprimentos de água: `numAstronautas * diasMissao * consumoAgua * (1 + reservaEmergencia/100)`
3. Suprimentos de comida: `numAstronautas * diasMissao * consumoComida * (1 + reservaEmergencia/100)`
4. Combustível necessário para a viagem (ida e volta): `(2 * distanciaLua / eficienciaCombustivel)`

Entrada:
O programa deve coletar todas as 10 variáveis acima do usuário.

Saída: 
O programa deve informar:
1. A quantidade total de oxigênio, água e comida necessária para a missão.
2. Se a quantidade de combustível necessária para a viagem (considerando ida e volta) excede a capacidade do tanque.
3. O peso total dos suprimentos e se isso pode ser uma preocupação para o lançamento (uma simplificação: considere um problema se o peso total dos suprimentos exceder 10% do peso do foguete).
'''

numAstronautas = int(input("Número de astronautas na missão: "))
diasMissao = float(input("Duração total da missão em dias: "))
consumoOxigenio = float(input("Consumo diário médio de oxigênio por astronauta em litros: "))
consumoAgua = float(input("Consumo diário médio de água por astronauta em litros: "))
consumoComida = float(input("Consumo diário médio de comida por astronauta em quilogramas: "))
pesoFoguete = float(input("Peso do foguete vazio em quilogramas: "))
eficienciaCombustivel = float(input("Eficiência do combustível (km/l): "))
distanciaLua = 384400
reservaEmergencia = float(input("Porcentagem de suprimentos extras para emergências: "))
capacidadeTanque = float(input("Capacidade máxima do tanque de combustível em litros: "))

suprimentos_oxigenio = numAstronautas * diasMissao * consumoOxigenio * (1 + reservaEmergencia/100)
suprimentos_agua = numAstronautas * diasMissao * consumoAgua * (1 + reservaEmergencia/100)
suprimentos_comida = numAstronautas * diasMissao * consumoComida * (1 + reservaEmergencia/100)
combustivel_necessario = (2 * distanciaLua / eficienciaCombustivel)

print("===============================")
print(f"A quantidade total de oxigênio necessário é: {suprimentos_oxigenio:.2f} litros")
print(f"A quantidade total de agua necessária é: {suprimentos_agua:.2f} litros") 
print(f"A quantidade total de comida necessária é: {suprimentos_comida:.2f} kg")

if capacidadeTanque >= combustivel_necessario:
    print("Tanque com capacidade suficiente.")
else:
    print("Tanque não tem a capacidade necessária.")

pesoF = pesoFoguete / 10

somaSuprimentos = suprimentos_comida + suprimentos_oxigenio + suprimentos_agua + (reservaEmergencia * 0.1)

if pesoF >= somaSuprimentos:
    print("O peso dos suprimentos não excede o limite")
else:
    print("O peso dos suprimentos excedem o peso limite")