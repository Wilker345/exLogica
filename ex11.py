#homem mais de 18, cabelo castanho e mulher 25...30 loiras
nh = int(0); nm = int(0)
h = []; m = []; ih = []; im = []; cm = []; ch = []
contH = int(0); contM = int(0)
s = str
f = int(0)
while(f !=1):
    s = input('Insira h para homem ou m para mulher: ')
    if (s == 'h'):
        ih[nh] = int(input('Insira a idade: ')) 
        ch[nh] = input('Selecione a cor de cabelo:\nCastanho: c\nLoiro: l\n Ruivo: r')
        if(ih[nh]> 18 & ch[nh] == 'c'):
            contH = contH + 1
        nh = nh + 1
    elif (s == 'm'):
        im[nm] = int(input('Insira a idade: ')) 
        cm[nm] = input('Selecione a cor de cabelo:\nCastanho: c\nLoiro: l\n Ruivo: r')
        if(25 < im[nm] < 30 & cm[nm] == 'l'):
            contM = contM + 1
        nm = nm + 1
    f = int(input('Insira 0 para continuar\nInsira 1 para terminar:'))
print('Saldo de homens: {}\nSaldo de mulheres: {}'.format(contH, contM))