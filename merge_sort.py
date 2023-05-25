def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

def merge_sort(data):
    n = len(data)
    if n > 1:
        mid = n // 2
        data_left = data[0:mid]
        merge_sort(data_left)
        data_right = data[mid:n]
        merge_sort(data_right)
        merge(data_left, data_right, data)
    return data

unsorted_numbers = [16,10,21,45]
print(merge_sort(unsorted_numbers))