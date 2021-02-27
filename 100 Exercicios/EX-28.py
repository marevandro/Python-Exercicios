from random import randint

num = randint(0,5)
print(f'-'*4,'JOGO DA ADVINHAÇÃO','-'*4)
print('Acerte o número que a maquina esta pensando.')

user = int(input('O escolha um número de 0 á 5: '))
if num == user:
    print(f'Voce acertou! A maquina tambem escolheu {num}')
else:
    print(f'VOCÊ ERROU! O número da maquina é {num}')
