'''Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.'''
salario = float(input("Qual seu salario? R$"))
desconto = salario + (salario*15/100)

print("Seu novo salario é: R${:.2f}".format(desconto))


produto = float(input("Qual o preço do produto? R$"))
prazo = produto + (produto*5/100)
avista = produto - (produto*13/100)

print ("O seu produto custa R${}\n"
       "Se for comprado avista ele fica por R${:.2f}.\n"
       "Tambem pode ser pago daqui a 30 dias e fica no valor de R${:.2f}.".format(produto, avista, prazo))
