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
Digite (1) e pague à vista dinheiro/cheque: ganhe 10% de desconto.
Digite (2) e pague vista no cartão: ganhe 5% de desconto.
Digite (3) e pague em até 2x no cartão: preço formalà vista no cartão: ganhe 5% de desconto
Digite (4) para pagamentos em 3x ou mais no cartão: tenha 20% de juros
Sua forma de pagamento: '''))