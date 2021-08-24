'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
#minha resolução
a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
if b + c > a and a + c > b and a + b > c:
    print('É possível formar um triangulo com essas medidas.', end='')
    if a == b == c:
        print('Temos um triângulo EQUILÁTERO.')
    elif a == b != c or b == c != a or c == a !=b:
        print('Temos um triângulo ISÓSCELES.')
    elif a != b and b != c and a != c:
        print('Temos um triângulo ESCALENO.')

else:
    print('Não é possível formar um triangulo com essas medidas.')
print('''
*
*
*     FIM''')

#resolução do curso
'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO!')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
'''
