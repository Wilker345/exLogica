# -*- coding: utf-8 -*-
timeA = int
timeB = int
saldo = int

timeA = input('Número de gols do time A: ')
timeB = input('Número de gols do time B: ')

if (timeA > timeB):
    saldo = int(timeA) - int(timeB)
elif (timeB > timeA):
    saldo = int(timeB) - int(timeA)
    
if (saldo == 0):
    print('Diferença de gols:', saldo, 'Status: empate')
elif (saldo > 3):
    print('Diferença de gols:', saldo, 'Status: goleada')
elif (3 > saldo > 0):
    print('Diferença de gols:', saldo, 'Status: partida normal')