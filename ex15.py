prova = ['a', 'c', 'e', 'b', 'd']
Joao = []; Maria = []; Carlos = []; notas = []; alternativa = []
mediaTurma = float
c = int(1)
nome = str
for i in range(3):
    acerto = int(0)
    if (c == 1):
        nome = 'Joao'
    elif (c == 2):
        nome = 'Maria'
    elif (c == 3):
        nome = 'Carlos'
        
    for o in range(5):
        alternativa.append(input('Insira a {}º alternativa de {}\nOPÇÕES: a, b, c, d, e:\n'.format(o+1, nome)))
        if (alternativa[o]==prova[o]):
            acerto = acerto + 2
    notas.append(acerto)
    acerto = 0
    c = c + 1
mediaTurma = float( notas[0]+notas[1]+notas[2] ) / 3
print('Nota João: {}'.format(notas[0]))
print('Nota Maria: {}'.format(notas[1]))
print('Nota Carlos: {}'.format(notas[2]))
print('Média da turma: {}'.format(mediaTurma))