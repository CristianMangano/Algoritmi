def quicksort(array, inizio, fine):
    if inizio < fine:
        perno = partiziona(array, inizio, fine)
        quicksort(array, inizio, perno - 1)
        quicksort(array, perno + 1, fine)

def partiziona(array, indice_inizio, indice_fine):
    pivot = array[indice_inizio]
    sx = indice_inizio + 1
    dx = indice_fine
    while sx <= dx:
        while sx <= dx and array[dx] > pivot:
            dx -= 1
        while sx <= dx and array[sx] < pivot:
            sx += 1
        if sx <= dx:
            array[sx], array[dx] = array[dx], array[sx]
    array[indice_inizio], array[dx] = array[dx], array[indice_inizio]
    return dx

array = [3,2,1]
quicksort(array, 0, len(array) - 1)
print(array)