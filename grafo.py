def bfs(grafo, vertice):
    nodi = grafo.keys()
    dizionario_visita = dict()
    for nodo in nodi:
        if nodo != vertice:
            dizionario_visita[nodo] = "da visitare"
    dizionario_visita[vertice] = "in visita"
    queue = list()
    queue.append(vertice)
    while queue:
        nodo = queue.pop(0)
        for v in grafo[nodo]:
            if dizionario_visita[v] == "da visitare":
                queue.append(v)
        print(nodo)
        dizionario_visita[nodo] = "visitato"

def visita_nodo(grafo, current_node, dizionario_visita):
    dizionario_visita[current_node] = "in visita"
    for nodo in grafo[current_node]:
        if dizionario_visita[nodo] == "non visitato":
            print(nodo)
            visita_nodo(grafo, nodo, dizionario_visita)
    dizionario_visita[nodo] = "visitato"

def attraversa_grafo(grafo):
    nodi = grafo.keys()
    dizionario_visita = dict()
    for nodo in nodi:
        dizionario_visita[nodo] = "non visitato"
    print(dizionario_visita)
    for current_node in nodi:
        if dizionario_visita[current_node] == "non visitato":
            visita_nodo(grafo, current_node, dizionario_visita)

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(grafo, 'A')