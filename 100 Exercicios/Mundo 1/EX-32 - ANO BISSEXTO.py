'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
#minha resolução
year = int(input("Qual ano você deseja analisar? \nDigite o ano: "))
if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
#explicando o ano bissexto
#https://escolakids.uol.com.br/matematica/calculo-do-ano-bissexto.htm
    print(f'O ano de {year} é BISSEXTO!')
else:
    print(f'O ano NÃO É BISSEXTO')

#resolução do curso
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 ==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
