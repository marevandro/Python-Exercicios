n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
result = n1 + n2
print (type(result))
'''Para tipos inteiros usamos int, lembrando que a classificação deve ser feita antes do input.
Numeros positivos, negativos ou nulos, são inteiros se não tiverem .'''

'''obs: Em Python os numeros não usamos a vírgula indicando que o algarismo a seguir 
pertence à ordem das décimas, ou casas decimais, é ultilizado o ponto (.) para fazer essa divisão. '''

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))
result = n1 + n2
print (result)
'''Para numeros com ponto flutuante ou numeros reais, que precisam de um ponto para separar das casas decimais.'''

n1 = bool(input("Digite um numero: "))
n2 = bool(input("Digite outro numero: "))
result = n1 + n2 == True
print (result)

n1 = str(input("Digite um numero: "))
n2 = str(input("Digite outro numero: "))
result = n1 + n2
print (result)
'''STR vem de string, na operação aparenta que eu vou somar, mas como
classifiquei minhas variáveis como str acontecera um concatenação.
Ex: "2" + "2" = 22'''


'''OBS: Lembrando que todas as variaveis devem ser especificadas,
se não, havera uma cocatenação.'''

# o tipo primitivo e definido por 'type' como no primeiro cáuculo
