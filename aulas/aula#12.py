'''Essa aula, vamos aprender como criar estruturas
condicionais aninhadas, usando os
comandos if.. elif.. else em programas Python.'''

nome = str(input('Qual é seu nome? ')).upper()
if nome == 'EREN':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome e bem popular no brasil.')
else:
    n = nome.capitalize()
    print('Que nome bonito {}!'.format(n))