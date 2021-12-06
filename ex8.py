a = input('Insira o início da contagem:')
b = input('Insira o final da contagem:')
c = int
if (a < b):
    c = int(a)
    while(c <= int(b)):
        print(c)
        c = c+1
if (a > b):
    c = int(a)
    while(c >= int(b)):
        print(c)
        c = c-1