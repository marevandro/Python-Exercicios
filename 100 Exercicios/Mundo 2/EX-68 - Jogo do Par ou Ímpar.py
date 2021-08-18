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

#solução do curso

from random import randint
v = 0
while True:
	jogador = int(input('Diga um valor: '))
	computador = randint (0,11)
	total = jogador + computador
	tipo = ' ' #PARA VALIDAR O 'TIPO' ELE JA PRECISA CONTER ALGUM VALOR
	while tipo not in 'PI' #ENQUANTO O 'TIPO' NÃO RECEBER NENHUM VALOR ELE VOLTA PRA ESSE LAÇO
		tipo = str(input('Par ou Impar? [P/I]')).strip().upper() [0] #ELIMINAR O ESPAÇO E JOGAR PARA MAIUSCULO VACILITANDO A VALIDAÇÃO
	print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
	print('DEU PAR' if total % 2 == 0  else 'DEU IMPAR')
	if tipo == 'P':
		if total % 2 == 0:
		print('Você VENCEU!')
		v += 1
	else:
		print('Você PERDEU!')
		break
	elif tipo == 'I':
		if total % 2 == 1:
			print('Você VENCEU!')
			v += 1
		else:
			print('Você PERDEU!')
			break
	print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes...')
