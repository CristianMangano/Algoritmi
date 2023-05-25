# def is_prime(object):
#     for number in range(2, object):
#         if object % number == 0:
#             return False
#     return True

# print(is_prime(6))

# fattori_primi = list()
# def is_prime(object):
#     for number in range(2, object):
#         if object % number == 0:
#             return False
#     return True
# def find_largest_prime_factor(number, largest_prime_factor=1):
#     if largest_prime_factor == number:
#         return max(fattori_primi)
#     if number % largest_prime_factor == 0 and is_prime(largest_prime_factor):
#         fattori_primi.append(largest_prime_factor)
#         return find_largest_prime_factor(number, largest_prime_factor + 1)
#     else:
#         return find_largest_prime_factor(number, largest_prime_factor + 1)
# print(find_largest_prime_factor(10))

# def find_smallest_multipe(*numbers):
#     minimo = list()
#     current = 1
#     while not minimo:
#         for number in numbers:
#             if current % number != 0:
#                 current = current + 1
#         minimo.append(current)
# print(find_smallest_multipe(range(1,11)))

# def find_smallest_multipe(numbers):
#     intervallo = list(numbers)
#     minimo = list()
#     teaser = list()
#     current = 2519
#     while not minimo:
#         teaser = [current % number for number in intervallo]
#         if any(teaser):
#             current += 1
#         else:
#             minimo.append(current)
#     return current
# print(find_smallest_multipe(range(1,11)))

# generator = (number for number in [0,1,2,3,4,5,6,7,8,9,10])
# for item in generator:
#     print(item)

# def is_even(stringa):
#     if len(stringa) % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even('casao'))

# def potenza(x, n):
#     if n == 0:
#         return 1
#     if n > 0:
#         return x * potenza(x, n - 1)
# print(potenza(2, 3))

# def is_prime(number):
#     for n in range(2, number):
#         if number % n == 0:
#             return False
#     return True
# def collection_primi(limit):
#     numeri_primi = list()
#     for number in range(2, limit + 1):
#         if is_prime(number):
#             numeri_primi.append(number)
#     return sum(numeri_primi)
# print(collection_primi(10))