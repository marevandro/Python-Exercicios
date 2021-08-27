lanche = ('Hambúrguer','Suco','Pizza','Pudim','Batata Frita')

#EXEMPLO 1 / FAZENDO A CHAMADA POR UM LAÇO SIMPLES
for c in lanche:
    print(c)

#EXEMPLO 2
for comida in lanche:
    print(f'Eu vou comer {comida}')

#EXEMPLO 3 / SEMPRE PRECISAR MOSTRAR A POSIÇÃO
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#EXEMPLO 4 
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#EXEMPLO 5 / SORTED PARA CRIAR UMA ORDEM ALFABETICA
print(sorted(lanche))

print('Comi pra caramba!')


#A TUPLA NÃO SOMA VALORES, CONCATENA 
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b	
print(c)
print(c.count(4))
print(c.index(8)) #MOSTRA A POSIÇÃO


#POSSO TER DADOS DE TIPOS DIFERENTES DENTRO DA TUPLA
#A TUPLA E IMUTÁVEL, MAS CONSEGUIMOS APAGAR USANDO O 'del', MAS NÃO CONSIGO DELETAR UM ITEM
