'''Escreva um programa que faça o computador
“pensar” em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo
computador. O programa deverá escrever na tela se o
usuário venceu ou perdeu.
'''

#minha resolução

from random import randint #não preciso import a biblioteca interia
import emoji
from time import sleep
num = randint(0,5)
print(f'-'*5,'JOGO DA ADVINHAÇÃO','-'*5)
print('Acerte o número que a maquina esta pensando.')
sleep(4)

user = int(input('O escolha um número de 0 á 5: '))
if num == user:
    print(f'Voce acertou! A maquina tambem escolheu {num}.', emoji.emojize(':dizzy_face:'))
    print()
else:
    print(f'VOCÊ ERROU! O número que eu escolhi foi {num}')
print('''
*
*
*''')
print(f'-'*5,'FIM DE JOGO','-'*5)

#resolução do curso

computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input("Emq que número eu pensei? "))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número e n')


