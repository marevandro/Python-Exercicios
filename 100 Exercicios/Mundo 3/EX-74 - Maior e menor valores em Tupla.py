''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

#minha resolução
from random import sample

#sample transforma uma string em uma lista e depois embaralha essa lista, nosso caso foi uma tupla
#o range faz a leitura de 30 valores, repetindo com o 'K' 5x
num = sample(range(30), k=5)
print(f'Os numeros aleatórios selecionados são: {num}')
print()
print(f'O maior valor da tupla é: {max(num)}')
print(f'O menor valor da tupla é: {min(num)}')

#resolução do curso
from random import randint
numeros = (randint(1,10),(randint(1,10),(randint(1,10),(randint(1,10),(randint(1,10))
print('Os valores sorteados foram: ',end='')
for n in numeros:
	print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
