'''Crie um programa que leia um número REAL qualquer pelo teclado e mostre
na tela a sua porção INTEIRA.
EX: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.'''

from math import floor, ceil
num = float(input("Digite um número: "))
print('O resultado inteiro do numero {} é {}'.format(num, floor(num)))
print('Arredondando pra cima, fica: {}.'.format(ceil(num)))