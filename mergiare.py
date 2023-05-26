def mergia(array, s1, s2):
  i, j = 0, 0
  while i + j < len(array):
    if j == len(s2) or i < len(s2) and s1[i] < s2[j]:
      array[i+j] = s1[i]
      i += 1
    else:
      array[i+j] = s2[j]
      j += 1
def mergesort(array):
  if len(array) > 1:
    left = array[:len(array)//2]
    right = array[len(array)//2:]
    mergesort(left)
    mergesort(right)
    mergia(array, left, right)
 
array = [9,8,7,6,5,4,3,2,1]
mergesort(array)
print(array)
