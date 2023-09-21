'''Uma loja vende piscinas retangulares de diferentes tamanhos. Com base na área da piscina, elas são classificadas em três categorias: Pequena, Média e Grande.
Entrada: 
O programa deve solicitar ao usuário a altura e a largura de um retângulo representando a piscina.
Saída:
O programa deve informar a área da piscina e sua categoria. 
Fórmula: 
Área = altura x largura
* Pequena: Até 10 m²
* Média: Mais de 10 m² até 30 m²
* Grande: Acima de 30 m²'''

comprimento = float(input("Qual o comprimento da piscina? (metros) "))
largura = float(input("Qual a largura da piscina? (metros) "))

area = float(comprimento * largura)

print(f"A área da piscina é de {area:.2f} m2")
if area <= 10:
    print("A piscina é da categoria Pequena.")
elif area > 10 and area <= 30:
    print("A piscina é da categoria Média.")
elif area > 30:
    print("A piscina é da categoria Grande.")