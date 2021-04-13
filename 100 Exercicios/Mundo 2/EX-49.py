'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário
 escolher, só que agora utilizando um laço for.'''

'''Desafio 9
Faça um programa que leia um número inteiro qualquer
e mostre na tela a sua tabuada.'''
import time
print('{:=^63}'.format('TABUADA'))
n = int(input('Digite um número: '))
print(f'Vamos verificar a tabuada do número {n}.')
time.sleep(2)
print('{: ^40} '.format('TABUADA DE MULTIPLICAÇÃO'))
for multi in range(1, 11):
    resultado = n * multi
    print(f'{n} * {multi} = {resultado}')
print('-'*10,'-','-'*10)

print('{: ^40} '.format('TABUADA DE DIVISÃO'))
for div in range(1, 11):
    resultado = float(n / div)
    print(f'{n} / {div} = {resultado:.1f}')
print('-'*10,'-','-'*10)

print('{: ^40} '.format('TABUADA DE ADIÇÃO'))
for adi in range(1,11):
    resultado = n + adi
    print(f'{n} + {adi} = {resultado}')
print('-'*10,'-','-'*10)

print('{: ^40} '.format('TABUADA DE SUBTRAÇÃO'))
if n == 1:
    for sub in range(2,11):
        resultado = sub - n
        print(f'{n} - {sub} = {resultado}')
else:
    for sub in range(n,11+n):
        resultado = sub - n
        print(f'{n} - {sub} = {resultado}')
print('-'*10,'Fim','-'*10)

#resolução do curso



