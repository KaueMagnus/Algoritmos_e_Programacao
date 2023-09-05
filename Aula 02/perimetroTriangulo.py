'''Perímetro de um Triângulo
   Solicite ao usuário os três lados de um triângulo. 
   Calcule o perímetro. Mostre o resultado.
'''

lado1 = float(input("Digite o valor do lado 1 (metros): "))
lado2 = float(input("Digite o valor do lado 2 (metros): "))
lado3 = float(input("Digite o valor do lado 3 (metros): "))

perimetro = lado1 + lado2 + lado3

print(f"O perimetro do triangulo é {perimetro:.1f}")