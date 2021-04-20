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