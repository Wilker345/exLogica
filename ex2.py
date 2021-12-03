# -*- coding: utf-8 -*-
anoAtual = int
anoNascimento = int
idade = int

anoAtual = input('Em que ano estamos? ')
anoNascimento = input('Em que ano voce nasceu? ')
idade = anoAtual - anoNascimento
print(idade, 'anos')
if (idade > 18):
    print('maior de idade')
elif (idade < 18):
    print('menor de idade')
