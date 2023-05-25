def heap_restore(array, partenza, dimensione):
    indice_di_partenza = partenza
    figlio_sinisrto = (2 * partenza) + 1
    figlio_destro = (2 * partenza) + 2
    if figlio_sinisrto < dimensione and array[figlio_sinisrto] > array[indice_di_partenza]:
        indice_di_partenza = figlio_sinisrto
    if figlio_destro < dimensione and array[figlio_destro] > array[indice_di_partenza]:
        indice_di_partenza = figlio_destro
    if indice_di_partenza != partenza:
        array[partenza], array[indice_di_partenza] = array[indice_di_partenza], array[partenza]
        heap_restore(array, indice_di_partenza, dimensione)

def build_maxHeap(array, dimensione):
    nodi_interni = (dimensione // 2) - 1
    for i in range(nodi_interni, -1, -1):
        heap_restore(array, i, dimensione)

def heapsort(array, dimensione):
    build_maxHeap(array, dimensione)
    for i in range(dimensione - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap_restore(array, 0, i)

array = [3,14,10,8,7,9,5]
heapsort(array, len(array))
print(array)
