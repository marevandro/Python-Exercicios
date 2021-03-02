'''Crie um programa que leia um número inteiro e mostre na
tela se ele é PAR ou ÍMPAR.
'''
#minha resolução
num = int(input("Digite um numéro qualquer: "))
resto_divisao = num % 2
if resto_divisao == 1:
    print(f'O número {num} é IMPAR!')
else:
    print(f'O número {num} é PAR!')
#resolução do curso
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O numero {} é ÍMPAR'.format(numero))
