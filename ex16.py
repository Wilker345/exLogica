b = ['']
l = int; cad = int
r = 'n'
   
def exibir():
   i = int
   for i in range (10):
      if (b[i] == ''):
         print ('[ b:{} ]'.format(i))
      elif (b[i] != ''):
         print('[ - - ]')

while (r == 'n'):
   exibir()
   cad = int(input('Reservar a cadeira da fila B:'))
   if (b[cad] == ''):
      b[cad] = 'x'
      print('Cadeira {} reservada'.format(cad))
   elif (b[cad] != ''):
      print('Local ocupado')
   r = input('Deseja reservar outro assento? s/n')

