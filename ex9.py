n = int(input('Quantos alunos existem na turma? '))
m = 0
estudantes = []
notas = []
for i in range(n):
  estudantes.append(input('Digite o nome do aluno: '))
  notas.append(input('Insira a nota do aluno: '))
  if (notas[i] > notas[i-1]):
      m = i
for x in estudantes:
  print("Aluno {}: {}".format(estudantes.index(x), x))
for x in notas:
  print("Nota {}: {}".format(notas.index(x), x))
print('maior nota, {}, foi do {}'.format(notas[m], estudantes[m]))