# -*- coding: utf-8 -*-
primeiraNota = float
segundaNota = float
media = float

primeiraNota = input('Primeira Nota: ')
segundaNota = input('Segunda Nota: ')
media = (float(primeiraNota) + float(segundaNota) )/ 2 
round(media, 2)
if (media > 9.0):
    print('Media:', media, 'Classificação: A')
elif (media > 8.0):
    print('Media:', media, 'Classificação: B')
elif (media > 7.0):
    print('Media:', media, 'Classificação: C')
elif (media > 6.0):
    print('Media:', media, 'Classificação: D')
elif (media > 5.0):
    print('Media:', media, 'Classificação: E')
elif (media < 5.0):
    print('Media:', media, 'Classificação: F')