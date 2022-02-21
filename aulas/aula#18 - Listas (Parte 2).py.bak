'''------------- Anotações -------------'''
#listas: mutaveis, podemos alterar
#representadas por colchetes []

lanche = ['Hamburguer','Suco','Pizza','Sorvete']


#comomando que adicionada um valor ao final da lista
lista.append('biscoito')


#posso adicionar um elemento em outra posição
#o que estava no 0, fica na posição 1 e assim sucessivamente
lista.insert(0,'cachorro-quente')


#função 'list'
#podemos converte uma string em uma lista.

>>> list("foo")
['f', 'o', 'o']

#Podemos converte tuplas em lista.

>>> list((1, 2, 3))
[1, 2, 3]
#Não podemos converter inteiros em uma lista porque o tipo int não é iterável.

#OBS: Mas podemos converter um inteiro em uma str e depois em uma lista

>>> list(123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable 


#comand para apagar elemntos
del lanche[3]

#metodo para apagar o ultimo elemento, mas com um paramento voce tambem pode eliminar qual obj quiser
lanche.pop()
lanche.pop(3)

#metodo que você não indica o indice e sim o valor que você deseja eliminar
#no caso se você quiser eliminar pelo contéudo.
#OBS: esse metodo retira apenas o 1° valor encontrado ou seja, se na lista existir mais de um, voce deve usar os laços de rep.
lanche.remove('Pizza') 


'''Caso eu queira remover um elemento que não existe ? 
Nesse caso eu verifico primeiro e depois retiro, usando um IF
'''
if 'Pizza' in lanche:
    lanche.remove('Pizza')
    
    
#metodo que alinha valores

valores = [8,2,5,4,9,3,0] #criando um variavel dentro do colchete, então é uma lista
#esse metodo vai organizar os valores
valores.sort()
#se for preciso os valores na ordem inversa, usamos um paramentro
valores.sort(reverse=True)



'''------------- Prática -------------'''
#Adicionando valores a uma lista. 

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o baslor {v}!')
print('Cheguei ao final da lista.')


#Ligação de uma lista com a outra

a = [2, 3, 4, 7]
b = a

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


#Criando uma copia

a = [2, 3, 4, 7]
#Relambrando a aula de fatiamento de str, aqui criamos uma copia 
b = a[:]

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
