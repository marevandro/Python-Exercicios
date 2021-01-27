'''Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente dessse ângulo'''
from math import sin, cos, tan
num = float(input('Digite o ângulo que você deseja: '))
seno = sin(num)
cosseno = cos(num)
tangente = tan(num)
print ('O seno do angulo {} é {:.2}'.format(num, seno))
print('O cosseno do ângulo {} é {:.2}'.format(num, cosseno))
print('A tangente do ângulo {} é {:.2}'.format(num, tangente))