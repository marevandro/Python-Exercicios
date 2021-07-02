'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


#minha resolução
print('-'*5,'Leitor de números','-'*5)
cont = 0
num = 0
soma = 0
while num != 999:
        num = int(input('Digite um número: '))
        print('Digitando 999 o programa vai parar')
        cont += 1
        soma = num + soma
        if num == 999:
            soma -= 999
            cont -=1
print(f'Você digitou {cont} números, a soma desse números é {soma}')  
print('FIM')


#resolução do curso
núm = cont = soma = 0
while núm != 999:
        núm = int(input('Digite um número [999 para parar]: '))
        cont += 1
        núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))        
