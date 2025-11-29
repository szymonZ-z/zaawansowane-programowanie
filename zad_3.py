def parzyste(liczby):
    for l in liczby:
        if l%2==0:
            print(l)
print(parzyste(range(10)))