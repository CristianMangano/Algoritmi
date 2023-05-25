
def maxheapify(array, indice_corrente):
    heapsize = len(array)
    radice = array[indice_corrente]
    left_child = 2 * indice_corrente + 1
    right_child = 2 * indice_corrente + 2
    if left_child < heapsize and array[left_child] > radice:
        radice = left_child
    if right_child < heapsize and array[right_child] > radice:
        radice = right_child
    if indice_corrente != radice:
        array[indice_corrente], array[radice] = array[radice], array[indice_corrente]
        maxheapify(array, radice)

heap = [3,14,10,8,7,9,5,2,4,1]
print(maxheapify(heap, 0))
