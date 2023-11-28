'''Crie uma função que calcule o montante final de um investimento com base no principal, taxa de juros e tempo.'''

def calcula_montante(principal, taxa_juros, tempo):
    
    taxa_decimal = taxa_juros / 100  
    montante_final = principal * (1 + taxa_decimal) ** tempo
    return montante_final


principal_inicial = float(input("Digite o capital inicial: "))
taxa_de_juros = float(input("Digite a taxa de juros: "))
meses = float(input("Quantos meses: "))

resultado = calcula_montante(principal_inicial, taxa_de_juros, meses)
print(f"O montante final do investimento é: R${resultado:.2f}")