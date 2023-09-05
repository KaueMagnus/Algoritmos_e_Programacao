'''Calcular e exibir o dobro de um numero caso ele seja positivo'''

numX = int(input("Digite um numero inteiro: "))

if numX >= 0:
    numX = numX * 2
    print(f"O dobro do numero e {numX}")

else:
    print("Numero negativo")    