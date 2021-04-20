'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

#minha resolução, nessa questão eu entendi a logicá mas não consegui terminar a resolução
print('-='*5,'10 TERMOS DE UMA PROGREÇÃO ARITIMETICA','=-'*5)
termo1 =int(input('Primeiro termo: '))
raz = int(input('Razão: '))
razão2 = termo1 * 1
for i in range(termo1, razão2, raz):
    print('{}'.format(i), end=' ->')

print('FIM!')

#resolução do curso
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range (primeiro, décimo + razão, razão):
	print('{}'.format(c), end='->')
print('ACABOU')


print('-=+'*15)
#Pra quem ta fazendo em 2020 fiz um pouco diferente espero que ajude ^^
print('-=' * 15)
print('   10 TERMOS DE UM P.A')
print('-=' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Qual é a razão da P.A: '))
décimo = primeiro + 10 * razão
for c in range (primeiro, décimo, razão):
    print(c, end = ' → ')
print('ACABOU')