def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def merge(sx, dx, arr):
    i, j = 0, 0
    while i + j < len(arr):
        if j == len(dx) or (i < len(sx) and sx[i] < dx[j]):
            arr[i + j] = sx[i]
            i += 1
        else:
            arr[i + j] = dx[j]
            j += 1

def mergesort(arr):
    l = len(arr)
    if l > 1:
        m = l // 2
        sx = arr[:m]
        dx = arr[m:]
        mergesort(sx)
        mergesort(dx)
        merge(sx, dx, arr)
    return arr

def insertionsort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i
        while j > 0 and arr[j - 1] > current:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = current

arr = [5, 2, 9, 1, 6, 3, 8]
sorted_arr = quicksort(arr)
print(sorted_arr)
sorted_mer_arr = mergesort(arr)
print(sorted_mer_arr)