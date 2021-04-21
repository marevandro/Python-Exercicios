'''Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente dessse ângulo'''

'''import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians((angulo)))
print('{}° tem o SENO de {:.2f}'.format(angulo, seno))
consseno = math.cos(math.radians(angulo))
print('{}° tem o cosseno de {:.2f}'.format(angulo, consseno))
tangente = math.tan(math.radians(angulo))
print('{}º tem a tangente de {:.2f}'.format(angulo, tangente))'''

#importando toda a biblioteca math


from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print ('O seno do angulo {} é {:.2}'.format(ang, seno))
print('O cosseno do ângulo {} é {:.2}'.format(ang, cosseno))
print('A tangente do ângulo {} é {:.2}'.format(ang, tangente))