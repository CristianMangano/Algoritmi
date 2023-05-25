def merge(left, right):
    merged = []
    i, j = 0, 0
    # Combina gli elementi delle due metà in ordine crescente
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Aggiungi gli eventuali elementi rimanenti della metà sinistra
    while i < len(left):
        merged.append(left[i])
        i += 1
    # Aggiungi gli eventuali elementi rimanenti della metà destra
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

def mergesort(array):
    dim = len(array)
    if dim > 1:
        n = dim // 2
        left_part = array[:n]
        right_part = array[n:]
        # Chiamata ricorsiva di mergesort sulle due metà
        left_part = mergesort(left_part)
        right_part = mergesort(right_part)
        # Effettua il merge delle due metà ordinate
        return merge(left_part, right_part)
    return array

def insertionsort(array):
    for i in range(1, len(array)):
        da_confrontare = array[i]
        j = i
        while j > 0 and da_confrontare < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = da_confrontare
    return array

array = [4, 3, 2, 1]
# sorted_array = mergesort(array)
print(insertionsort(array))