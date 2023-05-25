"""
visite in ampiezza e in profondita sui grafi
"""

def dfs(grafo, nodo, visitati):
    visitati[nodo] = 0  # * il nodo e' in analisi (in uno stato transitorio)
    for adiacenti in grafo[nodo]:
        if visitati[nodo] == -1:
            print(visitati[nodo])
            dfs(grafo, adiacenti, visitati)
    visitati[nodo] = 1

def procedura_visita(grafo):
    """ leggenda
    
    -1 non visitati
    0 in visita, transitorio
    1 visitati
    """
    visitati = dict()
    for node in grafo.keys():
        visitati[node] = -1
    for da_visitare in visitati.keys():
        if visitati[da_visitare] == -1:
            dfs(grafo, da_visitare, visitati)

grafo = {1:{2,5}, 2:{1,3,4,5}, 3:{2,4}, 4:{2,3,5}, 5:{1,2,4}}

print(procedura_visita(grafo))