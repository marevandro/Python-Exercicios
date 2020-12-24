'''Explicação técnica sobre alguns metodos.'''

digite = input('Digite algo: ')
print(type(digite))
print("Acusa o tipo primitivo.")
print("----------------------------------------")

print("isalum = ", digite.isalnum())
print("Acusa se contem numeros, (espaço)!#%&? Etc mostram o resultado falso.")
print("----------------------------------------")


print("isnumeric = ", digite.isnumeric())
print("verifique se todos os caracteres do texto são numéricos.")
print("----------------------------------------")


print("isalpha =", digite.isalpha())
print("Verifique se todos os caracteres do texto são letras.")
print("----------------------------------------")

print("isdigit = ",digite.isdigit())
print("Verdadeiro ou falso para numeros que sejam positivos. Apenas numero inteiros.")
print("----------------------------------------")

print("islower = ", digite.islower())
print("Verifica se a String tem o letra minuscula")
print("----------------------------------------")

print("isspace = ", digite.isspace())
print("Verifica se contem espaços")
print("----------------------------------------")
'''Vamos supor que peça para um campo ser preenchido e o usuário so da espaço e passa o campo, se
o valor for "False" um erro acontece.'''


print("issupper = ", digite.isupper())
print("Verifica se tem str maiuscula")
print("----------------------------------------")



print("========================FIM==========================")
