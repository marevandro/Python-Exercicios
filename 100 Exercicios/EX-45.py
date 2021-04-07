'''Crie um programa que faça o computador jogar Jokenpô com você.'''

#lembre que random significa aleatorio

#minha resolução
from random import randint
from time import sleep
aleatorio = randint(1,3)


print('---PEDRA, PAREL e TESOURA---')
print('''Escolha:
\033[1;33m(1)\033[m para PEDRA
\033[1;34m(2)\033[m para PAPEL
\033[1;35m(3)\033[m para TESOURA''')
print('Vamos ver quem ganha...')
sleep(2)
opcao = int(input('Qual sua opção? '))

if aleatorio ==1 and opcao == 3:
    opcao = 'TESOURA'
    print(f'Você escolheu {opcao}, a maquina escolheu PEDRA.')
    print('\033[31mPERDEDOR!\033[m')
elif aleatorio ==2 and opcao ==1:
    opcao = 'PEDRA'
    print(f'Você escolheu {opcao}, a maquina escolheu PAPEL.')
    print('\033[31mPERDEDOR!\033[m')
elif aleatorio == 3 and opcao == 2:
    opcao ='PAPEL'
    print(f'Você escolheu {opcao}, a maquina escolheu TESOURA.')
    print('\033[031mPERDEDOR!\033[m')
elif aleatorio ==1 and opcao ==2:
    aleatorio = 'PEDRA'
    print(f'Você escolheu PAPEL, a maquina escolheu {aleatorio} então...')
    print('\033[36mVOCÊ GANHOU\033[m')
elif aleatorio == 2 and opcao ==3:
    aleatorio='PAPEL'
    print(f'Você escolheu TESOURA, a maquina escolheu {aleatorio} então...')
    print('\033[36mVOCÊ GANHOU\033[m')
elif aleatorio == 3 and opcao ==1:
    aleatorio= 'TESOURA'
    print(f'Você escolheu PEDRA, a maquina escolheu {aleatorio} então...')
    print('\033[36mVOCÊ GANHOU\033[m')

#resolução do curso

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 3 ]TESOURA''')
jogador = int (input('Qual é a sua jogada? '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador ==0:
    if jogador == 0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador ==1:
    if jogador==0:
        print('COMPUTADOR VENCE')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador ==2:
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador ==1:
        print('COMPUTADOR VENCE')
    elif jogador==2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')