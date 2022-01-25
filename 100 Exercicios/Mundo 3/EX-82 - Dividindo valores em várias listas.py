''' Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

#minha resolução
lista = []
par=[]
impar=[]
while True:
  num = int(input('Digite um número: '))
  lista.append(num)
  if num % 2 == 0:
      par.append(num)
  elif num % 2 ==1:
    impar.append(num)
  resp = str(input('Deseja continuar? [S/N] '))
  if resp in 'Nn':
      break
print('=-/' *20)
print(f'Sua lista contem os valores {lista}')
if len(par) == 0:
  print('Sua lista não contem valores par.')
else:
  print(f'Dentro dessa lista eu tenho os valore par: {par}')
if len(impar)==0:
  print('Sua lista não contem valores impares. ')
else:
  print(f'E os valores impar são {impar}')
  
    
  #resolução do curso
num = list()
pares = list()
impares = list()
while True:
  num.append(int(input('Digite um número: ')))
  resp = str(input('Quer continuar? [S/N]'))
  if resp in 'Nn':
      break
for i, v in enumerate(num):
  if v % 2 == 0:
    pares.append(v)
  elif v % 2 == 1:
    impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
