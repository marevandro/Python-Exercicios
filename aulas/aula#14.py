#exemplo com for
'''for c in range(1,10):
    print(c)
print('FIM')'''

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
#os dois exemplos são a mesma coisa, usando o for o codigo fica ate menor, porem quando não sabemos a quantidade ?
#usamos o while para continuar no loop

n = 1
while n != 0: #enquanto a condição for dierente de 0, continue.
#pode ser conhecido como ponto de parada
    n = int(input('Digite um valor: '))
print('FIM')

#no segundo exemplo usamos str
r = 'S'
while r == 'S': #aqui o valor para continuar depende de uma igualdade e não uma diferença
    n= int(input('Digite um valor: '))
    r = str(input('Quer continuar ? [S/N]')).upper()
print('FIM')

num = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
print('Acabou')