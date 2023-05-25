def kruskal(grafo, grafo_minimo):
    albero_minimo = dict()
    foresta = dict()  # * l'insieme con le partizioni per scegliere nodi che non formano cicli nell'albero
    numeric = 0
    for nodo in grafo:
        foresta[numeric] = [nodo]
        numeric += 1
    numeri_arch = 0
    for nodo in grafo_minimo:
        vertice, vicino, peso = nodo
        find_in_giugle = find(foresta, vertice)
        find_in_giugle_2 = find(foresta, vicino)
        if find_in_giugle != find_in_giugle_2:
            foresta = merge(foresta, find_in_giugle, find_in_giugle_2)
            albero_minimo[numeri_arch] = (vertice, vicino, peso)
            numeri_arch += 1
    return albero_minimo

def merge(foresta, posizione1, posizione2):
    if posizione1 < posizione2:
        for node in foresta[posizione2]:
            foresta[posizione1].append(node)
        foresta[posizione2] = []    # * cancello la lista della partizione
    else:
        for node in foresta[posizione1]:
            foresta[posizione2].append(node)
        foresta[posizione1] = []
    return foresta

def find(foresta, vertice):
    for partition, nodi in foresta.items():
        if vertice in nodi:
            return partition

grafo_minimo = [
    ("F", "G", 1),
    ("A", "D", 1),
    ("E", "G", 2),
    ("B", "E", 2),
    ("C", "D", 2),
    ("A", "B", 2),
    ("D", "E", 3),
    ("B", "D", 3),
    ("A", "C", 4),
    ("C", "F", 4),
    ("D", "F", 5),
]

grafo = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'D': 3, 'E': 2},
    'C': {'A': 4, 'D': 2, 'F': 4},
    'D': {'A': 1, 'B': 3, 'C': 2, 'E': 3, 'F': 5},
    'E': {'B': 2, 'D': 3, 'G': 2},
    'F': {'C': 4, 'D': 5, 'G': 1},
    'G': {'E': 2, 'F': 1}
}

print(kruskal(grafo, grafo_minimo))