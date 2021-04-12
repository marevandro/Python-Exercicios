''' Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao
serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

'''2° Desafio:
Se for homem realiza todo o programa, se for mulher, informa que não precisa se alistar e encerra o 
programa. '''

#minha solução
#Na minha resolução, cheguei muito proximo a estutura montatda pelo professor, por isso deixei somente a dele.
#resolução do curso


from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = int(input('Qual seu sexo ? \nDigite (1) para masculino e (2) para feminino: '))
if sexo == 1:
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
else:
    print('''As mulheres estão isentas do alistamento obrigatório, mas isso não significa 
que elas estão proibidas de participar das forças armadas.''')