'''Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
#minha solução
cash = float(input('Qual o seu salário: R$'))
if cash <= 1250.00:
    cash = cash + (cash*15/100)
else:
    cash = cash + (cash*10/100)
print(f'Seu novo salario é: R${cash:.2f}')
#resolução do curso
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario*10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))



