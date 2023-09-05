'''Verificar se um caractere é uma vogal ou uma consoante.'''

letra = input("Digite uma letra: ")

if len(letra) == 1:
    letra = letra.lower()
    if letra in 'aeiou':
        print(f"A letra {letra} é uma vogal!")
    elif 'a' <= letra <= 'z':
        print(f"A letra {letra} é uma consoante!")
    else: 
        print(f"Digite uma LETRA!")
else:
    print("Digite apenas um caractere.")        

