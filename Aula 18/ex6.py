'''Implemente uma função que conte o número de vogais e consoantes em uma string.
'''

def contar_vogais_e_consoantes(frase):
    num_vogais = 0
    num_consoantes = 0
    
    vogais = set("aeiouAEIOU")
    
    for caractere in frase:
        if caractere in vogais:
            num_vogais += 1
        elif caractere.isalpha():
            num_consoantes += 1

    return num_vogais, num_consoantes

frase= input("Digite uma frase: ")
vogais, consoantes = contar_vogais_e_consoantes(frase)

print(f'Na frase "{frase}":')
print(f'Número de vogais: {vogais}')
print(f'Número de consoantes: {consoantes}')