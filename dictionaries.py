key = ('uno', 'due', 'tre')
dizionario = dict.fromkeys(key)

iteratore = iter([i for i in range(1, 4)])

for i in dizionario:
    dizionario[i] = next(iteratore)
print(dizionario)

dizionario2 = dict(quattro = 4, cinque = 5, sei = 6)

print('il primo dizionario')

for primo, secondo in zip(dizionario, dizionario2):
    print(primo, dizionario[primo])
    
print(dizionario2)

print('il secondo dizionario:')

for primo, secondo in zip(dizionario, dizionario2):
    print(secondo, dizionario2[secondo])