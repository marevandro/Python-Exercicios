'''Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo.'''

#minha resolução
#https://escolaeducacao.com.br/condicao-da-existencia-de-um-triangulo/
a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
if b + c > a and a + c > b and a + b > c:
    print('É possível formar um triangulo com essas medidas.')
else:
    print('Não é possível formar um triangulo com essas medidas.')
print('''
*
*
*     FIM''')

#resolução do curso
print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acuma NÃO PODEM FORMAR triângulo!')