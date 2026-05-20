from itertools import groupby

nomes = ["Ana", "Amanda", "Bruno", "Bia"]

nomes.sort()

for letra, alunos in groupby(nomes, key=lambda x: x[0]):
    print(f'Letra: {letra}')

    for aluno in alunos:
        print(f' - {aluno}')