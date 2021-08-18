'''FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, 
PARA CADA VALOR DIGITADO PELO USUÁRIO.
O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.'''


#minha resolução
print('-'*10,'TABUDA DE MULTIPLICAÇÃO','-'*10)
print('Se quiser sair do programa, digite um número negativo')
while True:
	num = int(input('Você deseja ver a tabuada de qual número ? '))
	if num > 0:
		break
		
	for i in range (1,11):
		mul = num * i 
		print(f'{num} x {i} = {mul}')
	print('-*-' * 10)
print('Número negativo, programa encerrado')


#resolução do curso
while True:
	n = int(input('Quer ver a tabuada de qual valor ? '))
	if n < 0:
		break
	print('-' * 30)
	for c in range(1, 11):
		print(f'{n} x {c} = {n*c}')
	print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
