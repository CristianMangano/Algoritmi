def prim(grafo, vertice):
    pass

grafo = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'D': 3, 'E': 2},
    'C': {'A': 4, 'D': 2, 'F': 4},
    'D': {'A': 1, 'B': 3, 'C': 2, 'E': 3, 'F': 5},
    'E': {'B': 2, 'D': 3, 'G': 2},
    'F': {'C': 4, 'D': 5, 'G': 1},
    'G': {'E': 2, 'F': 1}
}

# prim(grafo, 'A')

print(grafo['A']['B'])