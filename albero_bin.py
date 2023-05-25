"""
visita di un albero binario in ampiezza
"""

def somma_valori(albero, radice) -> int:
    if albero[radice]['figlio_destro'] or albero[radice]['figlio_sinistro']:
        numerate_foglie(albero, albero[radice]['figlio_sinistro'])
        numerate_foglie(albero, albero[radice]['figlio_destro'])

def numerate_foglie(albero, nodo, foglie = list()) -> int:
    if albero[nodo]['figlio_destro'] or albero[nodo]['figlio_sinistro']:
        numerate_foglie(albero, albero[nodo]['figlio_sinistro'], foglie)
        numerate_foglie(albero, albero[nodo]['figlio_destro'], foglie)
    if not (albero[nodo]['figlio_destro'] and albero[nodo]['figlio_sinistro']):
        foglie.append(nodo)
    return len(foglie)

def visita_ampiezza(albero, radice) -> list:
    queue = list()
    visitati = list()
    queue.append(radice)
    while queue:
        visitati.append(queue[0])
        current = queue.pop(0)
        if albero[current]['figlio_destro']:
            queue.append(albero[current]['figlio_destro'])
        if albero[current]['figlio_sinistro']:
            queue.append(albero[current]['figlio_sinistro'])
    return visitati

albero = {'A':{'genitore':None, 'figlio_destro': 'C', 'figlio_sinistro':'B'}, 'C':{'genitore':'A', 'figlio_destro': 'G', 'figlio_sinistro':'F'}, 'B':{'genitore':'A', 'figlio_destro': 'E', 'figlio_sinistro':'D'}, 'D':{'genitore':'B', 'figlio_destro':None, 'figlio_sinistro':None}, 'E':{'genitore':'B', 'figlio_destro':None, 'figlio_sinistro':None}, 'F':{'genitore':'C', 'figlio_destro':None, 'figlio_sinistro':None}, 'G':{'genitore':'C', 'figlio_destro':None, 'figlio_sinistro':None}}
visitati = visita_ampiezza(albero, 'A')
print(numerate_foglie(albero, 'A'))