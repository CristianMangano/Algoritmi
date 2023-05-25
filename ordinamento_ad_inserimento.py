def insertion_sort(cards):
    """
    funzione che ordina un array per inserimento
    """
    for j in range(0, len(cards)):
        current = cards[j]
        i = j - 1
        while i >= 0 and cards[i] > current:
            cards[i + 1] = cards[i]
            i -= 1
        cards[i + 1] = current

cards = [7,6,5,4,3,2,9,0]
insertion_sort(cards)
print(cards)