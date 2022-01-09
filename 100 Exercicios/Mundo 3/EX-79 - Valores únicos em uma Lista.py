'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''


#minha resolução

#crie um input para adicionar valores a lista
#depois crie um laço de rep para atribuir varios valores
#agora verifique se o valor ja foi adicionado
#por ultimo print a lista e deixe em ordem

adci = []
while True:
    valor=int(input('Digite um valor: '))
    if valor not in adci:
        adci.append(valor)
    else:
        print('Valor duplicado')
    resp = input('Deseja continuar? [S/N]: ').upper()
    while resp not in 'SN':
        resp = input('Continuar? [S/N]: ').upper()
    if resp == 'N':
        break
adci.sort()
print(f'Sua lista tem os numeros {adci}')


#resolução do curso

'''praticamente a mesma solução, apenas solucionou a questão da resposta, pois se eu desse um valor diferente de ‘S’ 
ele aceitava e continuava o programa'''

