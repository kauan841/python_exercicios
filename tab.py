tab =input('Digite um número: ')
int_tab = int(tab)
print(f'Tabuada do {int_tab}:')
for i in range(1, 11): 
    print(f'{int_tab} x {i} = {int_tab * i}')