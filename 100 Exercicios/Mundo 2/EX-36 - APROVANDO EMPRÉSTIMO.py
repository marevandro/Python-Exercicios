'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

#minha resolução
house = float(input('Qual o valor da casa ? \nPreço:'))
cash = float(input('Qual o valor do seu salario ? R$ '))
year = int(input('Quantos anos vai pagar? ')) #aqui resolvi colocar int pois a opçao e em anos, valor exato

year = year * 12
parcelas = house / year
menor_parcela = cash * 30 / 100

print(f'Para parcelar uma casa no valor {house} em {year}, você deve pagar uma parcela de {parcelas}')
if parcelas <= menor_parcela:
    print(f'Então esse emprestimo não compromete a sua renda de R$ {cash}.')
    print('Seu emprestimo foi APROVADO!')
else:
    print(f'Essa parcela no valor de R${menor_parcela} compromete mais de 30% da sua renda.')
    print('Seu emprestimo foi NEGADO!')
#resolução do curso

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos*12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <=minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')