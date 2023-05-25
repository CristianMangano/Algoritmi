def inizializza_albero(nodo = 'root'):
    albero_binario = dict()
    albero_binario[nodo] = {'genitore':None, 'figlioD':None, 'figlioS':None}
    return albero_binario
def aggiungi_figlio(albero_binario, genitore, nome_figlio, lato):
    if genitore in albero_binario and not albero_binario[genitore][lato]:
        albero_binario[genitore][lato] = nome_figlio
        albero_binario[nome_figlio] = {'genitore':genitore, 'figlioD':None, 'figlioS':None}
        # ! albero_binario[genitore][nome_figlio] = {'genitore':genitore, 'figlioD':None, 'figlioS':None}
def profondita(albero_binario, nodo):
    if not albero_binario[nodo]['genitore']:
        return 1
    if albero_binario[nodo]['genitore']:
        return 1 + profondita(albero_binario, albero_binario[nodo]['genitore'])

albero_binario = inizializza_albero('root')
aggiungi_figlio(albero_binario, 'root', 'gatti', 'figlioD')
aggiungi_figlio(albero_binario, 'root', 'cani', 'figlioS')
aggiungi_figlio(albero_binario, 'gatti', 'gatti brutti', 'figlioD')
aggiungi_figlio(albero_binario, 'gatti', 'gatti belli', 'figlioS')
aggiungi_figlio(albero_binario, 'cani', 'cani brutti', 'figlioD')
aggiungi_figlio(albero_binario, 'cani', 'cani belli', 'figlioS')

print(profondita(albero_binario, 'cani belli'))