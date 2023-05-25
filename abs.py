"""
verificarese due iste di tupe hanno gli stessi elementi
"""
def compara(t1, t2):
    lista = list()
    for tuplaT, tuplaT1 in zip(t1, t2):
        if tuplaT == tuplaT1:
            lista.append(tuplaT)
    print(lista)
listaT = [('a', 1), ('b', 2), ('c', 3)]
listaT1 = [('a', 1), ('b', 2), ('c', 3)]
compara(listaT, listaT1)