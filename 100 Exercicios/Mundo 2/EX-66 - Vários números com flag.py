
'''Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

#minha resolução
print('=*='*10)
conta = soma = 0
Print('Vamos somar os números e quando quiser parar digite 999 ')
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    conta += 1
print(f'Voce digitou {conta} números, a soma entre eles é: {soma}')
