'''Desenvolva um programa que leia as duas notas de um aluno,
 calcule e mostre a sua média.'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print("Sua media é {:.1f}".format(media))

'''Lembrando que existem ordens de precedencia, por isso
utilizamos parênteses.'''