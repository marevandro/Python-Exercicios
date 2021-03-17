'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''
#minha resolução
from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('Agora vamos comparar eles... ')
sleep (3)
if num1 > num2:
    print(f'O primeiro número digitado {num1}, é maior que {num2}')
elif num1 < num2:
    print(f'O segundo número digitado {num2}, é maior que {num1}')
else:
    print("Os dois números tem o mesmo valor!")

#resolução do curso
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')