'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''
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