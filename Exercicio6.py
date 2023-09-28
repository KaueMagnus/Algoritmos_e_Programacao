'''Fatorial de um Número: Peça ao usuário para inserir um número e calcule seu fatorial usando um loop while.
(Exemplo: 5! = 5x4x3x2x1 = 120)
'''

numero = int(input("Digite um número inteiro positivo: "))
numero_exibir = numero

if numero < 0:
    print("Impossivel fatorar")
    
elif numero == 0:
    print("O fatorial de 0 é 1")
    
else:
    fatorial = 1
    
    while numero > 0:
        fatorial *= numero
        numero -= 1

print(f"Fatorial de {numero_exibir} é igual a {fatorial}")