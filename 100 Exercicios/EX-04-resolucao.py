'''Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações possíveis
sobre ele.'''

digite = input('Digite algo: ')
print(type(digite))

digite = input('Digite algo: ')
print("O tipo primitivo desse valor é", type(digite))

print("So tem espaço?", digite.isspace())
print("É um numero ?", digite.isnumeric())
print("É alfabetico ?", digite.isalnum())
print("É alfanumérico ?", digite.isalnum())
print("Está em maiúsculas ?", digite.isupper())
print("Está em minúsculas ?", digite.islower())
print("Está captalizado ?", digite.istitle())
