'''Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações possíveis
sobre ele.'''

digite = input('Digite algo: ')
print("O tipo primitivo desse valor é", type(digite))

print("So tem espaço?", digite.isspace())
print("Verifica se contem somente espaços")
print("="*20)

print("É um numero ?", digite.isnumeric())
print("verifique se todos os caracteres do texto são numéricos.")
print("="*20)

print("É alfabetico ?", digite.isalpha())
print("Verifique se todos os caracteres do texto são letras.")
print("="*20)

print("É alfanumérico ?", digite.isalnum())
print("Verifica se os caracteres contem letras e numeros.")
print("="*20)

print("Está em maiúsculas ?", digite.isupper())
print("Verifica se as letras estão em maiúsculas")
print("="*20)

print("Está em minúsculas ?", digite.islower())
print("Verifica se as letras estão em minúsculas")
print("="*20)

print("Está captalizado ?", digite.istitle())
print("Verifica se a str não esta nem em maiúscula \n"
      "e nem em minúscula.")
print("="*20)
