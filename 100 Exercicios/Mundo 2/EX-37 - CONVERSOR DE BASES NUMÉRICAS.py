'''Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual
será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

'''
#minha resolção
from time import sleep
print('-'*10,'BASE DE CONVERSÃO','-'*10)
number = int(input('Digite um número inteiro qualquer: '))
print('Agora me diga qual base de conversão você quer.')
base = int(input('1 para binário\n2 para octal\n3 para hexadecimal\nDigite sua escolha: '))
print('Verificando...')
sleep(3)
if base == 1:
    print(f'O número {number} convertido para BINÁRIO é {bin(number)[2:]}.')
elif base ==2:
    print(f'O número {number} convertido para OCTAL é {oct(number)[2:]}')
elif base == 3:
    print(f'O número {number} convertido para HEXADECIMAL é {hex(number)[2:]}')
else:
    print('Opção errada! Tente novamente. ')
print('-'*10,'FIM','-'*10)
#lembrando sempre que o tratamento de str acontece nos colchetes []
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
