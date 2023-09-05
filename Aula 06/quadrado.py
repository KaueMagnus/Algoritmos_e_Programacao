'''Verificar se um número é um quadrado perfeito.'''

import math

numero = int(input("Digite um número: "))
raiz_quadrada = math.sqrt(numero)

if raiz_quadrada.is_integer():
    print(f"{numero} é um quadrado perfeito!")
    
else:
    print(f"{numero} não é um quadrado perfeito!")        
    