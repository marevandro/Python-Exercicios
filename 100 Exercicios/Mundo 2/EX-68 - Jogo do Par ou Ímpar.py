'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o 
total de vitórias consecutivas que ele conquistou no final do jogo.'''

#minha resolução
from random import randint
venc = 0
print('-=_'*6,'IMPAR_OU_PAR','-=_'*6)
while True:
	pc = randint(0, 100)

	play1 = int(input('Digite o número escolhido: '))
	escolha = input('Você escolhe Par ou Impar ? ').strip().upper()
	result = play1 + pc
	par_impar = result % 2
	if par_impar == 0:
		par_impar = 'PAR'
	else:
		par_impar = 'IMPAR'

	print(f'O jogador 1 escolheu {play1} á maquina escolheu {pc}. A soma deu {result} que é {par_impar}')
	
	if par_impar == 'PAR' and escolha == 'PAR':
		print ('Você GANHOU!')
		print('='*10)
		venc += 1
	elif par_impar == 'IMPAR' and escolha == 'IMPAR':
		print ('Você GANHOU!')
		print('='*10)
		venc += 1
	else:
		print('VOCÊ PERDEU!!!')
		break
print(f'Você conquistou {venc} vitorias')
