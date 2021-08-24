'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''


#minha solução
while True:
    print('{:=^45}'.format('CAIXA ELETRONICO DEV'))
    print('-\n'*2)
    valor = int(input('Digite o valor a ser sacado: R$'))
    
    
    print('Deseja realizar mais um saque?')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Sim [ S ] ou Não [ N ]: ')).strip().upper()[0]
        
    if sair == 'S':
        break
#resolução do curso
print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
	if total >= ced:
		total -= ced
		totced += 1
	else:
		if totced >0:
			print(f'Total de {totced} cédulas de R${ced}')
		if ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		totced = 0
		if total == 0:
			break
print('=') * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
	

