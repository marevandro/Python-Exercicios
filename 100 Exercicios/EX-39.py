''' Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao
serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


#minha solução
'''from datetime import date

hoje = date.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year

dia_nasc = int(input('Informe o dia do seu nascimento: '))
mes_nasc = int(input('Informe o mês: '))
ano_nasc = int(input('Por ultimo o ano: '))

if mes_nasc == 1:
    mes_nasc = ('Janeiro')
elif mes_nasc == 2:
    mes_nasc = ('Fevereiro')
elif mes_nasc == 3:
    mes_nasc = ('Março')
elif mes_nasc == 4:
    mes_nasc = ('Abril')
elif mes_nasc == 5:
    mes_nasc = ('Maio')
elif mes_nasc == 6:
    mes_nasc = ('Junho')
elif mes_nasc == 7:
    mes_nasc = ('Julho')
elif mes_nasc == 8:
    mes_nasc = ('Agosto')
elif mes_nasc == 9:
    mes_nasc= ('Setembro')
elif mes_nasc == 10:
    mes_nasc = ('Outubro')
elif mes_nasc == 11:
    mes_nasc = ('Novembro')
elif mes_nasc == 12:
    mes_nasc = ("Dezembro")
else:
    print('O ano so contem 12 messes, voce digitou esse valor errado! ')


print(f'A data atual é: {dia}/{mes}/{ano}')
idade = ano - ano_nasc
print(f'Voce tem {idade} anos de idade.')
if idade > 18:
    print('Você nasceu no dia {} de {} de {}')'''


#resolução do curso


from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))

