x = int(input("Fibonacci até X, determine X: "))
ultimo=1
penultimo=1


if (x==1) or (x==2):
    print("1")
else:
    count=3
    while count <= x:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
