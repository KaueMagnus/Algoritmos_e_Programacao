'''Média de Notas: Peça ao usuário para inserir uma série de notas e, em seguida, calcule a média das notas usando um loop while.
O loop deve continuar até que o usuário insira uma nota negativa.
'''

total = 0
quantidade = 0

nota = float(input(f"Digite a nota do aluno {quantidade + 1}: "))

while nota >= 0:
    total += nota
    quantidade += 1
    
    nota = float(input(f"Digite a nota do aluno {quantidade + 1}: "))
    if nota < 0:
        print("Encerrando...")
        break

media = total / quantidade
print(f"A média da turma com {quantidade} alunos é {media:.1f}")        