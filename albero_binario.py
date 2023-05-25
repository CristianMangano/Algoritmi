def add_root(node_name = 'root'):
    """
    inizializza la radice dell'albero
    """
    albero_binario = dict
    albero_binario[node_name] = {'parent' : None, 'left' : None, 'right' : None}
    return albero_binario

def add_child(albero_binario, genitore, nome_nodo, lato):
    """
    inserisce i figli a destra e a sinistra nell'albero
    """
    if genitore in albero_binario and not albero_binario[genitore][lato]:
        # * la condizione not garantisce che il genitore non abbia già un altro filgio in quel lato
        albero_binario[genitore][lato] = nome_nodo
        albero_binario[nome_nodo] = {'parent' : None, 'left' : None, 'right' : None}

def get_right_child(albero_binario, nodo):
    return albero_binario[nodo]['right']

def get_left_child(albero_binario, nodo):
    return albero_binario[nodo]['left']

def fratello_di_un_nodo(albero_binario, nodo):
    genitore = albero_binario[nodo]['parent']
    if nodo == albero_binario[genitore]['left']:
        return albero_binario[genitore]['right']
    else:
        return albero_binario[genitore]['left']

def is_root(albero_binario, nodo):
    if not albero_binario[nodo]['parent']:
        return True
    else:
        return False

def is_leaf(albero_binario, nodo):
    if not albero_binario[nodo]['left'] or not albero_binario[nodo]['right']:
        return True
    else:
        return False

def ottieni_tutti_i_figli_del_nodo(albero_binario, nodo):
    figli = list()
    if albero_binario[nodo]['left']:
        figli.append(albero_binario[nodo]['left'])
    if albero_binario[nodo]['right']:
        figli.append(albero_binario[nodo]['right'])
    return figli

def profondita(albero_binario, nodo):
    """
    funzione ricorsiva che calcola la profondità dell'albero
    """
    if not albero_binario[nodo]['parent']:
        return 1
    if albero_binario[nodo]['parent']:
        return 1 + profondita(albero_binario, albero_binario[nodo]['parent'])





# ? si tratta di un dizionario dentro un dizionario più generale che è l'albero?

# * inizializzare un albero esplicitamente: albero_binario = {'root':{'genitore':None, 'dx':None, 'sx':None}}
# * albero binario con due nodi:
# * gen = genitore
# * tree = {'root':{'gen':None, 'dx':'child', 'sx':None}, 'child':{'gen':'root', 'dx':None, 'sx':None}}
# * dove 'dx' sta per 'figlio a destra', e sx 'figlio a sinistra'