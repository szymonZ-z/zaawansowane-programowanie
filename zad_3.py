def parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


print(parzyste(range(10)))
