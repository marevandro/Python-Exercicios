''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.'''
#minha resolução
from random import randint
computer = randint(0,10)
player = 0
cont = 1 #começaremos com essa variável em 1, ja vamos ter uma tentativa de cara
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
player = int(input("Em qual número eu pensei? "))
if player == computer:
    print('\033[1;32mPARABÉNS!\033[m Você conseguiu me vencer de primeira!')#[1;32 Verde
else:
    while computer != player:
        if computer < player:
            #[1;33m Amarelo
            print('\033[1;33mMenos que isso...\033[m')
            player = int(input('\033[1;31mTente novamente: \033[m')) #[1;33 Vermelho
        else:
            #[1;93 Amarelo Claro
            print('\033[1;93mMais que isso...\033[m')
            player = int(input('\033[1;31mTente novamente: \033[m')) #[1;33 Vermelho
        cont += 1
    print(f'''\033[34mFIM! Voce conseguiu!
Você tentou {cont}x para acertar. \033[m''')

#resoluçãom do curso
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegur adivinhar qual foi ?')
acertou = False
palpites = 0
while not acertou:
   jogador = int(input('Qual é seu palpite? '))
   palpites += 1
   if jogador == computador:
       acertou = True
   else:
       if jogador < computador:
            print('Mais...Tente mais uma vez.')
       elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))