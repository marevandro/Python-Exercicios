'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

'''
#minha resolução
'''from time import sleep
name = input('Digite uma frase: ')
print('Vamos verificar se essa frase é um palindromo...')
sleep(2)
trecho = name.split()
for c in range (0, trecho):
    '''
#resolução do curso
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)+1, -1, -1):
#len(junto)-1, tenho que ir da ultima a primeira letra
#', -1', ele vai ate a primeira letra, mas no tratamento de str não queremos que ele leia 0 por isso -1
#', -1', depois vai voltando uma letra
    inverso *= junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
