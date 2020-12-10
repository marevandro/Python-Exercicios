'''Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações possíveis
sobre ele.'''

digite = input('Digite algo: ')
print(type(digite))
#acusa o tipo primitivo.
print(digite.isalnum())
#acusa se todos os caracteres do texto são alfanuméricos, (espaço)!#%&? Etc mostram o resultado falso.
print(digite.isnumeric())
#verifique se todos os caracteres do texto são numéricos.
print(digite.isalpha())
#Verifique se todos os caracteres do texto são letras.
print(digite.isdecimal())
#
print(digite.isdigit())
print(digite.isidentifier())
print(digite.islower())
print(digite.isprintable())
print(digite.isspace())
print(digite.istitle())
print(digite.isupper())