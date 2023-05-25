"""
dato un semplice albero implementare la visita in profondità in pre-ordine
"""

def deep(albero, nodo):
    if albero[nodo]['genitore']:
        return 1 + deep(albero, albero[nodo]['genitore'])
    return 1

def crea_albero(node = 'G'):
    albero = {node : {'genitore' : None, 'figlio_destro' : None, 'figlio_sinistro' : None}}
    return albero

def aggiungi_nodo(albero, nodo, genitore, verso):
    if nodo not in albero and genitore in albero and not albero[genitore][verso]:
        albero[nodo] = {'genitore' : genitore, 'figlio_destro' : None, 'figlio_sinistro' : None}
        albero[genitore][verso] = nodo

def preorder(binary_tree, node_name, visited = list()):
    visited.append(node_name)
    sotto_albero_sx = binary_tree[node_name]['figlio_sinistro']
    sotto_albero_dx = binary_tree[node_name]['figlio_destro']
    if sotto_albero_sx or sotto_albero_dx:
        preorder(binary_tree, sotto_albero_sx, visited)
        preorder(binary_tree, sotto_albero_dx, visited)
    return visited

def postordine(albero, nodo, visitati = list()):
    if albero[nodo]['figlio_sinistro'] or albero[nodo]['figlio_destro']:
        postordine(albero, albero[nodo]['figlio_sinistro'])
        postordine(albero, albero[nodo]['figlio_destro'])
    visitati.append(nodo)
    return visitati

def altezza(albero, radice):
    if radice:
        sottoalbero_sx = altezza(albero, albero[radice]['figlio_sinistro'])
        sottoalbero_dx = altezza(albero, albero[radice]['figlio_destro'])
        return max(sottoalbero_sx, sottoalbero_dx) + 1
    else:
        return 0

def altezza_bfs(albero, radice):
    queue = [(radice, 1)]
    h = 0
    while queue:
        current, current_height = queue.pop(0)
        h = max(h, current_height)
        if albero[current]['figlio_sinistro']:
            queue.append((albero[current]['figlio_sinistro'], current_height + 1))
        if albero[current]['figlio_destro']:
            queue.append((albero[current]['figlio_destro'], current_height + 1))
    return h

tree = crea_albero()
aggiungi_nodo(tree, 'F', 'G', 'figlio_destro')
aggiungi_nodo(tree, 'E', 'G', 'figlio_sinistro')
# lista_nodi = preorder(tree, 'G')
# print(lista_nodi)
# lista_nodi_post = postordine(tree, 'G')
# print(lista_nodi_post)
print(altezza_bfs(tree, 'G'))
print(altezza(tree, 'G'))
print(deep(tree, 'G'))