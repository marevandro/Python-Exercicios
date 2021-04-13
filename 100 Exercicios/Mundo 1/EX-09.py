'''Faça um programa que leia um número inteiro qualquer
e mostre na tela a sua tabuada.'''

num = int(input("Digite um numero: "))
print("-"*20)
print("A tabuada do numero {} é: ".format(num))
print("{} x 1 = {}".format(num, num*1))
print("{} x 2 = {}".format(num, num*2))
print("{} x 3 = {}".format(num, num*3))
print("{} x 4 = {}".format(num, num*4))
print("{} x 5 = {}".format(num, num*5))
print("{} x 6 = {}".format(num, num*6))
print("{} x 7 = {}".format(num, num*7))
print("{} x 8 = {}".format(num, num*8))
print("{} x 9 = {}".format(num, num*9))
print("-"*20)

for tabuada in range(1,11):
    resultado = n*tabuada
    print(f'{n} * {tabuada} = {resultado}')