'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

#minha resolução
lista=[]
while True:
  num = int(input('Digite um número: '))
  lista.append(num)
  resposta = str(input('Deseja continuar? [S/N]: ')).upper()
  if resposta == 'N':
    break
lista.sort(reverse=True)
print('=-'*20)
print(f'Foram digitados {len(lista)} números.')
print(f'A lista ordenada de forma decrescente é {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da sua lista')
else:
    print('A sua lista não contém o número 5.')

----------------------------------------------------------------------------------------
#resolução do curso
valores = []
while True:
  valores.append(int(input('Digite um valor: ')))
  resp = str(input('Quer continuar ?[S/N] '))
  if resp in 'Nn':
    break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
  print('O valor 5 não foi encontrado na lista!')

