'''Faça um programa que calcule a soma entre todos os
números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
#minha resolução
for inte in range  (1,501):
    if inte % 3 == 0:
        total = inte + inte
print(f'Solução de todos os números somados é {total}')
'''Não implementei a regra de acumulador, por isso a resolução funciona mas não retorna a quantidade certa.
Entenda que a numéração que você precisa não é o resultado dos multiplos de 3, mas sim, a soma desses números.
É bem obivio mas deve ser dito. '''

#resolução do curso
soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 ==0:
        cont = cont + 1
        #ou cont += c
        soma = soma + c
        #ou soma += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
