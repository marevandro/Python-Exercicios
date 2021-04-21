''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

'''

num = int(input('Informe um número: '))
nu = str (num)
print(f'Nosso numero é {num}.')
print(f'Sua unidade é: {nu[3:]}')
print(f'Sua dezena é: {nu[2:]}')
print(f'Sua centena é: {nu[1:]}')
print(f'Sua milhar é: {nu[0]}')

print("""Esxite uma falha nessa resolução. Se não digitar os 4 numeros ele
não mostra as outras unidades. Porém a resolução do Guanabara mosta uma formula 
 sem modificar as str e sim com numeros inteiros.""")

num1= int(input("Informe uma milhar: "))
uni = num // 1 % 10
de = num // 10 % 10
ce = num // 100 % 10
mi = num // 1000 % 10
print(f'Sua unidade é: {uni}')
print(f'Sua dezena é: {de}')
print(f'Sua centena é: {ce}')
print(f'Sua milhar é: {mi}')
