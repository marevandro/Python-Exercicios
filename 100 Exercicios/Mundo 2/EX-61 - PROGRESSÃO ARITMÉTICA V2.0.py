'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de 
uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

#primeiro = int(input('Primeiro termo: '))
#razão = int(input('Razão: '))
#for c in range(1, 10, 2):
#    print(f'{c}')
#print('Acabou.')


#resolução do curso
print ('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}')
    termo += razão
    cont += 1
