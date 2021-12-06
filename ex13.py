valores = [5]
s = float(0); dcinco = int(0); nulos = int(0); spar = float(0); m = float
c = 0;
for i in range(5):
    valores.append(float(input('Insira o {}º valor:'.format(c+1))))
    if (valores[c]%5):
        dcinco = dcinco+1
    if (valores[c] == 0):
        nulos = nulos + 1
    if (valores[c]%2):
        spar = spar + valores[c]
    s = s + valores[c]
    c = c + 1
m = s / 5
print('soma: {}\nmedia de todos: {}\n{} sao divisiveis por 5\n{} sao nulos\nsoma de todos os pares:{}'
      .format(s, m, dcinco, nulos, spar))