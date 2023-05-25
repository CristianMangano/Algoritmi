def profondita(albero, nodo):
    if albero[nodo]['genitore']:
        return 1 + profondita(albero, albero[nodo]['genitore'])
    if not albero[nodo]['genitore']:
        return 0

def calcola_altezza(albero, radice):
    if not radice:
        return 0
    altezza_sinistra = calcola_altezza(albero, albero[radice]['figlio_sx'])
    altezza_destra = calcola_altezza(albero, albero[radice]['figlio_dx'])
    return 1 + max(altezza_sinistra, altezza_destra)

def conta_foglie(albero, radice, foglie = list()):
    if albero[radice]['figlio_dx']:
        conta_foglie(albero, albero[radice]['figlio_dx'], foglie)
    if albero[radice]['figlio_sx']:
        conta_foglie(albero, albero[radice]['figlio_sx'], foglie)
    if not (albero[radice]['figlio_dx'] or albero[radice]['figlio_sx']):
        foglie.append(radice)
    return foglie

albero = {
    'A': {'genitore': None, 'figlio_dx': 'B', 'figlio_sx': 'C'},
    'B': {'genitore': 'A', 'figlio_dx': 'D', 'figlio_sx': 'E'},
    'C': {'genitore': 'A', 'figlio_dx': 'F', 'figlio_sx': None},
    'D': {'genitore': 'B', 'figlio_dx': None, 'figlio_sx': None},
    'E': {'genitore': 'B', 'figlio_dx': 'G', 'figlio_sx': 'H'},
    'F': {'genitore': 'C', 'figlio_dx': 'I', 'figlio_sx': 'J'},
    'G': {'genitore': 'E', 'figlio_dx': None, 'figlio_sx': None},
    'H': {'genitore': 'E', 'figlio_dx': 'K', 'figlio_sx': None},
    'I': {'genitore': 'F', 'figlio_dx': None, 'figlio_sx': None},
    'J': {'genitore': 'F', 'figlio_dx': None, 'figlio_sx': None},
    'K': {'genitore': 'H', 'figlio_dx': None, 'figlio_sx': None}
}

print(calcola_altezza(albero, 'A'))