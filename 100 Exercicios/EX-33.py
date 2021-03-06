'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
#minha primeira resolução
#from time import sleep
#print('Vamos ver qual o mairo e menor número dessa sequencia...')
#sleep(2)
'''num1 = int(input('Digite o primeiro numéro: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))'''

'''Meu primerio erro:
if (num1 > num2) and (num1> num3):
    print(f'O maior número dentro dessa sequência é {num1}')
if (num2 > num1) and (num2 > num3):
    print(f'O maior número dentro dessa sequência é {num2}')
else:
    print(f'O maior número dentro dessa sequência é {num3}')
Mas dessa forma eu faria duas verificações e se as duas fossem verdadeiras iriam mostrar o resultado.
No outro exemplo foi compreendido que se uma condição não fosse a verdadeira eu iria pra uma que não e verdadeira, 
depois disso entrava no IF novamente.
'''
'''if (num1 > num2) and (num1> num3):
    print(f'O maior número dentro dessa sequência é {num1}')
else:
    if (num2 > num1) and (num2 > num3):
        print(f'O maior número dentro dessa sequência é {num2}')
    else:
        print(f'O maior número dentro dessa sequência é {num3}')'''
#depois compreendemos o elif e ficou mais bonito
'''if (num1 > num2) and (num1 > num3):
    print(f'O maior número dentro dessa sequência é {num1}')
elif (num2 > num1) and (num2 > num3):
    print(f'O maior número dentro dessa sequência é {num2}')
else:
    print(f'O maior número dentro dessa sequência é {num3}')'''
#minha segunda resolução
'''numeros = str(input('Digite 3 numerações: ')).split()
a1 ,b2, c3 = int(numeros[0]), int(numeros[1]), int(numeros[2])
maior = max(a1, b2, c3)
minimo = min(a1, b2, c3)
print(f'O maior numero dessa sequência é {maior}.')
print(f'O menor numero dessa sequência é {minimo}.')'''

#minha terceira resolução
'''digite1 = int(input('Digite o primeiro número: '))
digite2 = int(input('Digite o segundo número: '))
digite3 = int(input('Digite o terceiro número: '))
maior_valor = max(digite1, digite2, digite3)
menor_valor = min(digite1, digite2, digite3)
print(f'O maior numero dessa sequência é {maior}.')
print(f'O menor numero dessa sequência é {minimo}.')'''
#mas sem utilizar if e else

#resolução do curso
a= int(input('Primerio valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a #verificando quem é menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a #verificando o maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

