"""
invertire un dizionario: un altro modo
"""
def inverti(dizionario):
    inverso = dict()
    listaDeiValori = list(dizionario.values())
    listaDelleChiavi = list(dizionario.keys())
    for chiave, valore in zip(listaDeiValori, listaDelleChiavi):
        if chiave not in inverso:
            inverso[chiave] = [valore]
        else:
            inverso[chiave].append(valore)
    return inverso
dizionario = {'matteo':66, 'francesco':88, 'gaetano':88}
dizionarioInverso = inverti(dizionario)
print(dizionarioInverso)