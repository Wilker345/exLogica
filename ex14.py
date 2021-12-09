import random
times = []
for i in range(3):
    times.append(input('Insira o nome do {}º time: '.format(i+1)))
for o in range(3):
    for p in range(3):
         if (times[o] != times[p]):
            a = random.randrange(0, 4); b = random.randrange(0, 4)
            print('{}  [ {} ] x [ {} ]  {}'.format(times[o], a, b, times[p]))