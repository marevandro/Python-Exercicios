'''Faça um programa que leia um número inteiro e mostre na tela
seu sucessor e seu antecessor'''

n1 = int(input("Digite um número: "))
sucessor = n1 + 1
antecessor = n1 - 1
print("Você escolheu o numero {}, seu sucessor é "
      "{} e seu antecessor é {}.".format(n1, sucessor, antecessor))
