''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''


#solução do curso
núm = (int(input('Digite um número: ')),
	   int(input('Digite outro número: ')),
	   int(input('Sigite mais um número: ')),
	   int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
	print(f'O valor 3 apareceu na {núm.index(3)+1}º posição')
else:
	print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ',end='')
for n in núm:
	if n % 2 == 0:
		print(n, end='')
		
#minha resolução

num1 = tuple(input('Digite o 1° número: '))
num2 = tuple(input('Digite o 2° número: '))
num3 = tuple(input('Digite o 3° número: '))
num4 = tuple(input('Digite o 4° número: '))

todos = num1 + num2 + num3 + num4

print(f'O valor 9 apareceu {todos.count(9)}x')
if 3 in todos:
	print(f'O valor 3 esta na posição {todos.index(3)+1}° posição')
else:
	print('O valor 3 não foi digitado nenhuma vez')
for par in todos:
	if n % 2 == 0:
		print(n ,) 
		
Validar pq minha resolução ainda da erro

