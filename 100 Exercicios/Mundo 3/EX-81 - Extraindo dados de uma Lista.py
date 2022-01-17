'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = input('Continuar ? [S/N] ').upper()
    if resp == 'N':
        break
lista.sort()
cont = len(lista)
print(lista,cont,lista.sort(reverse=True))
