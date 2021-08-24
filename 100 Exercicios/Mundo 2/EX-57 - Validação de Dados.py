#minha resolução
sexo = 1
while sexo != 'M' or 'F'
    sexo = input('Digite seu sexo: ').upper()
    if sexo != 'M' or 'F'
        print('Esse valor e invalido, digite outro valor.')
else:
    print(f'Seu sexo é {sexo}')
#resolução do curso
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
