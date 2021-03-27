'''A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
#minha resolução
from datetime import date
from time import sleep
nome = input('Qual seu nome ?').strip()
nome = nome.title()
nasc = int(input('Ano do seu nascimento: '))
data = date.today().year
age = data - nasc
print('Vamos verificar qual é a categoria do atleta...')
sleep(2)
if age <= 9:
    print(f'{nome}, com {age} de idade, você participa da categoria MIRIM.')
elif age <= 14:
    print(f'{nome}, com {age} de idade, você participa da categoria INFANTIL.')
elif age <= 19:
    print(f'{nome}, com {age} de idade, você participa da categoria JUNIOR.')
elif age <= 25:
    print(f'{nome}, com {age} de idade, você participa da categoria SÊNIOR.')
else:
    print(f'{nome}, com {age} de idade, você ja esta na categoria ADULTO.')
#resolução do curso
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
