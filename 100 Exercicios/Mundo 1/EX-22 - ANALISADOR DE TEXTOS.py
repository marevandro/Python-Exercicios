'''Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao tdo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome:')).strip()
print(f'Ola {nome}.')
print(f'Seu nome em maiúsculo fica {nome.upper()}!')
print(f'Seu nome em minúsculo fica {nome.lower()}!')

#aqui contamos quantos espaços tem e diminuimos
print(f"Seu nome tem no total de {len(nome) - nome.count(' ')} letras")

print('-'*23)
print("""No curso foi abordado como resolver essa segunda parte usando o metodo "find",
mas não ficou claro, quem poder ajudar no entendimento eu agradceço.
Usei a segunda abordagem, separando e contando com o len.""")
print('Sintaxe: print(f"Seu nome tem {nome.find(' ')} letras")')
print('-'*23)

primeiro = nome.split()
print(f'Seu primeiro nome tem {len(primeiro[0])} letras')
