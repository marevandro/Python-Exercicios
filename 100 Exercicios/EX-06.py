'''Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.'''

num = int(input("Digite um numero: "))
print("Você escolheu o número: {}".format(num))
print("O dobro de {} é {}".format(num, (num*2)))
print("O triplo de {} é {}".format(num, (num*3)))
print("A raiz quadrada de {} é {:.2f}".format(num, (num**(1/2))))
print("Usando a função 'pow'. {:.2f}".format(pow(num,(1/2))))

'''#lembrando que se não for necessario usar esses calculos em outras situações,
não preciso guardar esses valores em uma variável.'''