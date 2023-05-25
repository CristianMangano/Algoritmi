def heapBuil(array, dimensione):
    indice = (dimensione // 2) - 1
    for i in range(indice, -1, -1):
        maxheap_restore(array, i, dimensione)

def maxheap_restore(array, partenza, dimensione):
    indice_del_massimo = partenza
    left = 2 * partenza + 1
    right = 2 * partenza + 2
    if left < dimensione and array[left] > array[partenza]: # * se il valore figlio sinistro è nel vettore ed è maggiore del valore del padre
        indice_del_massimo = left  # * prendi come elemento indice_del_massimo l'indice del figlio
    if right < dimensione and array[right] > array[indice_del_massimo]: # * se il figlio destro è anche più grande del figlio sinistro
        indice_del_massimo = right # * prendi questo indice
    if partenza != indice_del_massimo:    # * se quindi il indice_del_massimo valore non è l'indice inizialmente passato
        array[partenza], array[indice_del_massimo] = array[indice_del_massimo], array[partenza]   # * scambio tra la partenza di input e la partenza massima
        maxheap_restore(array, indice_del_massimo, dimensione)

def heapsort(array, dimensione):
    heapBuil(array, dimensione)
    for i in range(dimensione - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        maxheap_restore(array, 0, i)

array = [3, 14, 10, 8, 7, 9, 5]
maxheap_restore(array, 1, len(array))
# maxheap_restore(array, 0, len(array))
print(array)