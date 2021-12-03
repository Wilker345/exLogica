# -*- coding: utf-8 -*-
anoAtual = int
anoNascimento = int
idade = int

anoAtual = input('Ano atual: ')
anoNascimento = input('Ano de nascimento: ')
idade = anoAtual - anoNascimento
print(idade, 'anos')
if (idade > 18):
    print('Idade: ', idade, 'Apto a obter uma carteira de motorista')
elif (idade < 18):
    print('Idade: ', idade, 'Inapto a obter uma carteira de motorista')