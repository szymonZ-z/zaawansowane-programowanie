# Wersja 1
def mnozenie_for(liczby):
    for i in range(len(liczby)):
        liczby[i] *= 2
    return liczby


print(mnozenie_for([2, 3, 4, 5, 6]))


# Wersja 2
def mnozenie_skladana(liczby):
    return [liczba*2 for liczba in liczby]


print(mnozenie_skladana([2, 3, 4, 5, 6]))
