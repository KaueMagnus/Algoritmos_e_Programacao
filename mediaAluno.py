'''Escrever um programa que lê as 3 notas obtidas por ele em provas.
Para cada aluno, calcular a média de aproveitamento, usando a fórmula:
	     MA = (Nl + N2 + N3) / 3                   
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = float((nota1 + nota2 + nota3) / 3)

if media < 4:
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média do aluno: {media:.2f}")
    print(f"Conceito E - REPROVADO")

elif media >= 4 and media < 6:
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média do aluno: {media:.2f}")
    print(f"Conceito D - REPROVADO")

elif media >= 6 and media < 7.5:
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média do aluno: {media:.2f}")
    print(f"Conceito C - APROVADO")

elif media >= 7.5 and media < 9:
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média do aluno: {media:.2f}")
    print(f"Conceito B - APROVADO")

elif media >= 9:
    print(f"Média do aluno: {media:.2f}")
    print(f"Conceito a - APROVADO")
        