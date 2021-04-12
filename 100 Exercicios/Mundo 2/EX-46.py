'''Faça um programa que mostre na tela uma contagem regressiva para o
estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

#minha resolução
from time import sleep
for c in range(10,0, -1):
    print(c)
    sleep(1)
print('BUM! BUM! BUM!')
print('-'*10,'FELIZ ANO NOVO','-'*10)

#resolução do curso
'''A resolução ficou parecida com a minha.'''