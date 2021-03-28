'''Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formalà vista no cartão: 5% de desconto

– 3x ou mais no cartão: 20% de juros'''

produto = float(input('Preço do produto: '))
print('''*
*
*''')
print('-'*10,'FORMA DE PAGAMENTO','-'*10)
pagamento = int(input(''' - Opções de pagamento: 
\033[33mDigite (1)\033[m e pague à vista dinheiro/cheque: \033[34mganhe 10% de mdesconto.\033[m
\033[33mDigite (2)\033[m e pague vista no cartão: \033[34mganhe 5% de desconto.\033[m
\033[33mDigite (3)\033[m e pague em até 2x no cartão: preço formalà vista no cartão: \033[34mganhe 5% de desconto\033[m
\033[33mDigite (4)\033[m para pagamentos em 3x ou mais no cartão: \033[31mtenha 20% de juros\033[m
Sua forma de pagamento: '''))
print('-'*15)
if pagamento == 1:
    desconto = (produto*10/100)
    produto = produto - desconto
    print('v', produto)