
def massimo(albero, radice, lista_nodi = list()):
    if radice and radice not in lista_nodi:
        lista_nodi.append(radice)
        massimo(albero, albero[radice]['sinistro'], lista_nodi)
        massimo(albero, albero[radice]['destro'], lista_nodi)
    return max(lista_nodi)

def massimo_iterativo(albero_di_ricerca, radice):
    nodi_visitati = list()
    while albero_di_ricerca[radice]['destro']:
        nodi_visitati.append(albero_di_ricerca[radice]['destro'])
        radice = albero_di_ricerca[radice]['destro']
    return nodi_visitati.pop()

def ricerca(albero_di_ricerca, radice, chiave):
    if radice and chiave < radice:
        return ricerca(albero_di_ricerca, albero_di_ricerca[radice]['sinistro'], chiave)
    if radice and chiave > radice:
        return ricerca(albero_di_ricerca, albero_di_ricerca[radice]['destro'], chiave)
    if chiave == radice:
        return True
    if not radice:
        return False

albero = {33:{'genitore':None, 'destro':35, 'sinistro':31}, 35:{'genitore':33, 'destro':None, 'sinistro':None}, 31:{'genitore':33, 'destro':None, 'sinistro':None}}
# print(massimo(albero, 33))
# print(massimo_iterativo(albero, 33))
print(ricerca(albero, 33, 38))