'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

#minha solução
total_com = mais_mil = menor_produto = 0
maior = menor = 0
print('-=-'*7,'MERCADINHO DEV','-=-'*7)
while True:
    nome_produ = str(input('Digite o nome do produto: '))
    valor = float(input('Agora digite o valor: R$ '))
    result = ' '
    while result not in 'SN':
        result = input('Deseja continuar comprando [S/N] ?' ).strip().upper()
    total_com += valor
    if valor < 1000:
        mais_mil += 1
	
	
	if total_com == 1:
		  reult_produ = nome_produ
	    maior  = valor
  else:
      if maior < valor:
      result_produ = nome_produ
			
	
    print('---\n'*3)
	
	
    if result == 'N':
        break
print(f'Total de produtos {total_com}')
print(f'Total de produtos acima de R$ 1000,00 é {mais_mil}')
print(f'O produto mais barato é {reult_produ}')

