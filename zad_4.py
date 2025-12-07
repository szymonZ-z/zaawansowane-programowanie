def co_drugi(liczby):
    for i in range(len(liczby)):
        if i % 2 == 0:
            print(liczby[i])


co_drugi(range(1, 11))
