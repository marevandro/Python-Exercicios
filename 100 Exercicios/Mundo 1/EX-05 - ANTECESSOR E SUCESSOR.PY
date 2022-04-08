'''Faça um programa que leia um número inteiro e mostre na tela
seu sucessor e seu antecessor'''

#resolução do curso

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

#minha resolução
num = int(input('Digite um numero: '))
print(f'O valor {num} tem como seu antecessor o número {num-1} e seu sucessor o número {num+1}.')