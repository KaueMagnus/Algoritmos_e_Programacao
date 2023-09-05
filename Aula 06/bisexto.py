'''Verificar se o ano é bisexto'''

ano = int(input("Digite o ano: "))

verificar = ano % 4

if verificar == 0:
    print(f"O ano de {ano} é bisexto!")

else:
    print(f"O ano {ano} não é bisexto!")    