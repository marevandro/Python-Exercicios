'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

#minha resolução
numpar = 0

for par in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2==0:
        numpar = num + numpar
        listapar= numpar
    else:
   '''A construção da repetição esta ok, ele ja soma os pares.'''
