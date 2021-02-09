'''Um professor quer sortear um dos seus quatro alunos para
 apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos
  e escrevendo na tela o nome do escolhido.'''
import random
n1= str(input("Digite o nome do primerio aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))

alunos = [n1, n2, n3, n4]
escolha = random.choice(alunos)
print("Entre os alunos, o escolhido foi: {}.".format(escolha))

"""Devemos categorizar o tipo de variável, para transforma em uma lista e depois
fazer a função random ler a lista. """