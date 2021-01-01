'''Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.'''
salario = float(input("Qual seu salario? R$"))
desconto = salario + (salario*15/100)

print("Seu novo salario é: R${}".format(desconto))