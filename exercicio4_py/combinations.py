from itertools import combinations
nomes = ["Kauan", "Lucas", "Ana"]

print('Combinações de 2 itens:')
for combo in combinations(nomes, 2):
    print(combo)