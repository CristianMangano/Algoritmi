def kruskal(grafo):
    edges = list()
    visited = set()
    albero_minimo, partizione = dict(), dict()
    for nodo in grafo:
        for vicino, peso in grafo[nodo].items():
            if (nodo, vicino) not in visited and (vicino, nodo) not in visited:
                edges.append((nodo, vicino, peso))
                visited.add((nodo, vicino))
    quicksort(edges, 0, len(edges) - 1)
    numero_di_nodi = 0
    for archi in edges:
        nodo, vicino, peso = archi
        trova_nodo = find(partizione,nodo)
        trova_vicino = find(partizione, vicino)
        if trova_nodo != trova_vicino:
            # ! partizione = merge(partizione, trova_nodo, trova_vicino)
            albero_minimo[numero_di_nodi] = (nodo, vicino, peso)
            numero_di_nodi += 1

def find(partizione, nodo):
    for vertice, vicino in partizione.items():
        if nodo in vicino:
            return vertice

def quicksort(edges, inizio, fine):
    if inizio < fine:
        pivot = partizione_ordina_archi(edges, inizio, fine)
        quicksort(edges, inizio, pivot - 1)
        quicksort(edges, pivot + 1, fine)

def partizione_ordina_archi(lista, inizio, fine):
    pivot = lista[inizio][2]
    sx = inizio + 1
    dx = fine
    while sx <= dx:
        while lista[dx][2] > pivot:
            dx -= 1
        while sx <= dx and lista[sx][2] <= pivot:
            sx += 1
        if sx <= dx:
            lista[dx], lista[sx] = lista[sx], lista[dx]
    lista[inizio], lista[dx] = lista[dx], lista[inizio]
    return dx

grafo = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'D': 3, 'E': 2},
    'C': {'A': 4, 'D': 2, 'F': 4},
    'D': {'A': 1, 'B': 3, 'C': 2, 'E': 3, 'F': 5},
    'E': {'B': 2, 'D': 3, 'G': 2},
    'F': {'C': 4, 'D': 5, 'G': 1},
    'G': {'E': 2, 'F': 1}
}

archi_ordinati = kruskal(grafo)
print(archi_ordinati)