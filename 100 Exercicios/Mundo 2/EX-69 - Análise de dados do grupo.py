'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o 
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

#minha solução
maior = cont_hom = menor_mulher = 0 
while True:
	print('-=+'*5,'CADASTRO','-=+'*5)
	ida = int(input('Qual sua idade: '))
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]

	if ida > 18:
		maior += 1					
	if sexo == 'M':
		cont_hom += 1
	if sexo == 'F' and ida < 20:
		menor_mulher += 1
	print('Deseja continuar com mais um cadastro ?')
	result = str(input('Sim [S] e Não [N]: ')).strip().upper()
	if result == 'N':
		break
print('''O cadastro conta com {} a cima da 18 anos;
O total de {} homens cadastradors;\n
O total de {} mulheres com menos de 20 anos'''.format(maior, cont_hom,menor_mulher))


