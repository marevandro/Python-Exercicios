#listas: mutaveis, podemos alterar
#representadas por colchetes []



#comomando que adicionada um valor ao final da lista
.append('biscoito')


#posso adicionar um elemento em outra posição
#o que estava no 0, fica na posição 1 e assim sucessivamente
.insert(0,'cachorro-quente')


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



