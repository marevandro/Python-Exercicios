'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

#minha solução
total_com = mais_mil = menor_produto = maior = 0
result_produto = ' '
print('-=-'*7,'MERCADINHO DEV','-=-'*7)
while True:
    nome_produ = str(input('Digite o nome do produto: '))
    valor = float(input('Agora digite o valor: R$'))
    result = ' '
    while result not in 'SN':
        result = input('Deseja continuar comprando [S/N] ?' ).strip().upper()[0]
    total_com += valor
    if valor > 1000:
        mais_mil += 1
    
    
    if total_com == 1 or valor < menor_produto:
        menor_produto = valor
        maior  = valor
        result_produ = nome_produto
            
    
    print('---\n'*3)
    
    
    if result == 'N':
        break
print(f'Total de produtos {total_com:.2f}')
print(f'Total de produtos acima de R$ 1000,00 é {mais_mil}')
print(f'O produto mais barato é {reult_produ}')


#resolução do curso
total = totmil = menor = cont = 0
barato = ' '
while True:
	produto = str(input('Nome do Produto: '))
	preço = float(input('Preço: R$'))
	cont += 1
	total += preço
	if preço > 1000:
		totmil += 1
	
	#esse bloco se repete 
	#if cont == 1:
	#	menor = preço
	#	barato = produto
	#else:
	#	if preço < menor:
	#		menor = preço
	#		barato = produto
	
	#segunda opção
	if cont == 1 or preço < menor:
		menor = preço
		barato = produto 
	
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {} custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

