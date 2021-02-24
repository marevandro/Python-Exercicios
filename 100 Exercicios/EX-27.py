'''Faça um programa que
leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente.'''

print('''Não e necessário utilizarmos o len nessa situação, ficou entendido no
último exercício que a leitura pode ser vista de trás pra frente utilizando -1''')
next = input("Aperte enter para continuar: ")
name = str(input('Digite seu nome completo: ')).strip()
n1 = name.split()
print(f"Seu primeiro nome é {n1[0]}.")
print(f"Seu ultimo nome é {n1[-1]}.")

next = input("""Vamos verificar a resolução do curso em video.
Aperte ENTER: """)

n = str(input('Digite seu nome completo: '))
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))