"""
algoritmi di ottimizzazione o algoritmi greedy (minimizzazione)
pesi non negativi

"""

def distanza_minima(grafo, vertice):
    """
    ritorna un dizionario con tutte le distanze minime da vertice. Attenzione: non 
    ritorna il cammino, mi dice soltato la distanza minima che esiste tra vertice e qualsiasi
    altro nodo. Per trovare il cammino minimo devo usare un'altra funzione che si appoggia a questa
    
    """
    predecessori = list() # TODO creare la lista dei predecessori per trovare il cammino minimo
    nodi = grafo.keys()
    dizionario_distanza_min = dict()
    for nodo in nodi:
        if nodo != vertice:
            dizionario_distanza_min[nodo] = [float("inf"), "da visitare"]
    dizionario_distanza_min[vertice] = [0, "in visita"]
    queue = [(0, vertice)]
    while queue:
        distanza, nodo = queue[0][0], queue[0][1]
        queue = queue[1:]
        dizionario_distanza_min[nodo][1] = "visitato"
        for nodo_corrente in grafo[nodo]:
            if dizionario_distanza_min[nodo_corrente][1] == "da visitare": # * se non ho ancora visitato il nodo, e sto parlando dei nodi tra parentesi graffe che hanno come chiave 'A'
                peso_arco = grafo[nodo][nodo_corrente] # * estraggo l'informazione del peso dell'arco, dove nodo = 'A' mentre nodo_corrente varia tra {'B', 'C', 'D'}
                distanza_totale = distanza + peso_arco # * calcolo la distanza totale
                if distanza_totale < dizionario_distanza_min[nodo_corrente][0]: # * scelta greedy
                    dizionario_distanza_min[nodo_corrente][0] = distanza_totale # * inserisce un numero al nodo che da inf ad esempio, assume un valore sempre minore
                    queue.append((distanza_totale, nodo_corrente)) # * aggiungo il prossimo nodo da visitare
    return dizionario_distanza_min

grafo = {
    'A': {'B': 2, 'C': 4, 'D': 1},
    'B': {'A': 2, 'D': 3, 'E': 2},
    'C': {'A': 4, 'D': 2, 'F': 4},
    'D': {'A': 1, 'B': 3, 'C': 2, 'E': 3, 'F': 5},
    'E': {'B': 2, 'D': 3, 'G': 2},
    'F': {'C': 4, 'D': 5, 'G': 1},
    'G': {'E': 2, 'F': 1}
}

print(distanza_minima(grafo, 'A'))