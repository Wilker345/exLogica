# -*- coding: utf-8 -*-
primeiraNota = float
segundaNota = float
media = float

primeiraNota = input('Primeira Nota: ')
segundaNota = input('Segunda Nota: ')
media = float( (primeiraNota + segundaNota) / 2 )
if (media > 7.0):
    print('Media: ', media, 'ALUNO APROVADO')
elif (media < 7.0):
    print('Media: ', media, 'ALUNO REPROVADO')