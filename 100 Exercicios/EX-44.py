'''Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal

– 3x ou mais no cartão: 20% de juros'''
#minha resolução
print('-*-'*7,'MERCADINHO','-*-'*7)
produto = float(input('PREÇO DAS SUAS COMPRAS: R$'))
print('''*
*
*''')
print('-'*10,'FORMA DE PAGAMENTO','-'*10)
pagamento = int(input(''' - Opções de pagamento: 
\033[33mDigite (1)\033[m e pague à vista dinheiro/cheque: \033[34mganhe 10% de mdesconto.\033[m
\033[33mDigite (2)\033[m e pague vista no cartão: \033[34mganhe 5% de desconto.\033[m
\033[33mDigite (3)\033[m e pague em até 2x no cartão: preço \033[7mnormal\033[m 
\033[33mDigite (4)\033[m para pagamentos em 3x ou mais no cartão: \033[31mtenha 20% de juros\033[m
Sua forma de pagamento: '''))
print('-'*15)
if pagamento == 1:
    desconto = (produto*10/100)
    desconto = produto - desconto
    print(f'''Você escolheu o pagamento à vista. 
O valor de R${produto:.2f}, fica R${desconto:.2f}''')
elif pagamento ==2:
    desconto = produto - (produto*5/100)
    print(f'''Você escolheu o pagamento à vista no cartão de credito.
O valor de R${produto:.2f}, fica R${desconto:.2f}''')
elif pagamento ==3:
    print('Parcelando em duas vezes o valor continua o mesmo.')
elif pagamento ==4:
    print('Agora você pode parcelar em até 6x com \033[31m20% de juros.\033[m')
    parcelamento = int(input('Quantidade de parcelas: '))
    juros = (produto*20/100) + produto
#poderia ter criado outra variavel para guardar o numero de parcelas e depois dividir o preço
    if parcelamento == 3:
         parcelamento = juros / 3
         print(f'Com o juros, preço aumenta para R${juros:.2f} dividido em 3 parcelas de R${parcelamento:.2f}')
    elif parcelamento == 4:
         parcelamento = juros / 4
         print(f'Com o juros, preço aumenta para R${juros:.2f} dividido em 4 parcelas de R${parcelamento:.2f}')
    elif parcelamento == 5:
         parcelamento = juros / 5
         print(f'Com o juros, preço aumenta para R${juros:.2f} dividido em 4 parcelas de R${parcelamento:.2f}')
    elif parcelamento == 6:
         parcelamento = juros / 6
         print(f'Com o juros, preço aumenta para R${juros:.2f} dividido em 4 parcelas de R${parcelamento:.2f}')
    else:
        print('''ATENÇÃO!
Não podemos comportar esse valor de parcelas. Obrigado.''')
else:
    print('Você não escolheu a forma de pagamento. ')
#solução do curso

print('{:=^40}.'.format('LOJAS GUANABARA'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinherio/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual á a opção?'))
if opção ==1:
    total = preço - (preço*10/100)
elif opção ==2:
    total = preço - (preço*5/100)
elif opção ==3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em {}x de R${:.2f} SEM JUROS'.format(parcela))
elif opção ==4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))


