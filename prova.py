
def confronto_valori(a, b):
    if a == b:
        return True
    else:
        return False

def confronto_riferimenti(a, b):
    if a is b:
        return True
    else:
        return False

a = [1,2,3]
b = a

print(confronto_riferimenti(a, b))
print(confronto_valori(a, b))