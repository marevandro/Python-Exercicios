'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
 e quantas já são maiores.'''
#minha resolução
from datetime import date
print('\033[31m-'*10,'=','\033[31m-\033[m'*10)
maior = 0
menor = 0
hoje = date.today().year
for c in range(1,8):
    idade = int(input(f'Qual o ano de nascimento dessa {c}° pessoa?\n Digite aqui: '))
    if hoje - idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'''No total {maior} pessoas atingiram a maior idade e {menor} pessoas são de menor.''')
print('\033[31m-'*10,'FIM','\033[31m-\033[m'*10)

#resolução do curso
#minha solução foi muito parecida, deixei a minha solução23





