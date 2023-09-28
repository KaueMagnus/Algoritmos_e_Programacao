'''Múltiplos de 3: Use um loop while para imprimir todos os múltiplos de 3 de 1 a 50.'''

contador = 1

print("MULTIPLOS DE 3:")
while contador <= 50:
    multiplo = contador % 3
    contador += 1
    
    if multiplo == 0:
        print(contador)
    
    

        