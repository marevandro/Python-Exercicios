'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

#minha resolução
numpar = 0

for par in range(1,7):
    number = int(input(f'Digite {par}° valor: '))
    if number % 2==0:
        numpar += number
print (f'A soma de todos os valores pares é {numpar}')
#resolução do curso

soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Diigte o valor {}: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont +=  1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))
