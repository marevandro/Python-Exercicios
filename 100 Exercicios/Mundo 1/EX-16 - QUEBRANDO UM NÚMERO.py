'''Crie um programa que leia um número REAL qualquer pelo teclado e mostre
na tela a sua porção INTEIRA.
EX: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.'''

'''
from math import floor, ceil, trunc
num = float(input("Digite um número: "))
print('O resultado inteiro do numero {} é {}'.format(num, floor(num)))
print('Arredondando pra cima, fica: {}.'.format(ceil(num)))

num1 = float(input('Digite um número: '))
print ('O resultado inteiro do número {} é {}.'.format(num1, trunc(num1)))
'''
#sem usar uma biblioteca para esse exercicio.
num = float(input("Digite um valor: "))
print('O valor digitanto foi {} e sua porção inteira é {}.'.format(num, int(num)))

