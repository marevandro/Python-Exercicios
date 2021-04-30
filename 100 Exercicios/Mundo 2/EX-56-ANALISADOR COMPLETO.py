'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
#cont_idade = 0
#for c in range (1,5):
#    name = input(f'Digite o nome da {c}° pessoa: ')
#    idade = int(input('Qual a sua idade?'))
#    sexo = int(input('''Qual seu sexo?
#(1) Masculino (2) Feminino'''))

#if c ==1:
    #cont_idade = idade + 1
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher20 = 0
for p in range (1,5):
    print('------------{}° PESSOA---------'.format(p))
    nome = str(input('Nome')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade > 20:
        total_mulher20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher20))
