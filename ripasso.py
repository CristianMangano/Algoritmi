
def build_max_heap(array, dimensione):
    nodi_interni = (dimensione // 2)
    for i in range(nodi_interni, -1, -1):
        max_heap_restore(array, i, nodi_interni)

def max_heap_restore(array, posizione, dimensione):
    massimo = posizione
    figlio_sinistro = (posizione * 2) + 1
    figlio_destro = (posizione * 2) + 2
    if figlio_destro < dimensione and array[massimo] < array[figlio_destro]:
        massimo = figlio_destro
    if figlio_sinistro < dimensione and array[massimo] < array[figlio_sinistro]:
        massimo = figlio_sinistro
    if massimo != posizione:
        array[posizione], array[massimo] = array[massimo], array[posizione]
        max_heap_restore(array, massimo, dimensione)

def heapsort(array, dimensione):
    build_max_heap(array, dimensione)
    for i in range(dimensione - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heap_restore(array, 0, i)
    return array

array = [33,27,82,10,9]
print(heapsort(array, len(array)))
print(array)