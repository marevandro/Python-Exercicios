'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

#minhas solução

#lendo 5 valores numericos e guardando em uma lista
num = []
for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {cont}:')))
#mostrar qual o maior e menor valor digitado e suas posições
print("=-"*30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} que se encontra na posição {num.index(max(num))}')
print(f'O menor valor digitado foi {min(num)} que se encontra na posição {num.index(min(num))}')  
'''Existe um erro nessa solução, ainda não resolvido.
A questão de quando existem valores iguais, não é possível replicar
'''

#resolução do curso

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print ('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
