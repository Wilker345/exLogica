massa = float
altura = float

massa = input('Insira massa(em Kg): ')
altura = input('Insira altura(em m): ')

imc = ( float(massa) / float(altura * altura) )
print('IMC = ', imc)
if (imc < 17):
    print('muito abaixo do peso')
elif (17 < imc < 18.5):
    print('abaixo do peso')
elif ( 18.5 < imc < 25):
    print('peso ideal')
elif (25 < imc ):
    print('sobrepso')