'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = 'M','F'
while sexo != 'M' and sexo != 'F':
    sexo = input('''Qual o seu sexo ?
(M) para masculino e (F) para feminino: ''').upper()
    if sexo != 'M' and sexo != 'F':
        print('Esse valor não foi aceito, tenti novamente.')
    else:
        if sexo == 'M':
            sexo = 'MASCULINO'
        else:
            sexo = 'FEMININO'
        print(f'Seu sexo é {sexo}')
