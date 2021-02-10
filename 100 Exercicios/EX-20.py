'''O mesmo professor do desafio 19 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
n1 = str(input("Qual o primeiro aluno: "))
n2 = str(input("Qual o segundo aluno: "))
n3 = str(input("Qual o terceiro aluno: "))
n4 = str(input("Qual o quarto aluno: "))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print(f'Alista dos alunos é:{alunos} ')