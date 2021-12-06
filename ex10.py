f = int(0)
while(f !=1):
    a = int(input('Selecione 1 para contar de 1 a 10.\nSelecione 2 para contar de 10 a 1.\nSelecione 3 pra encerrar:'))
    c = int(1)
    if (a == 1):
        while(c <= 10):
            print(c)
            c = c+1
    if (a == 2):
        c = int(10)
        while(c >= 1):
            print(c)
            c = c-1
    if(a == 3):
        print('fim.')
        f = int(1)