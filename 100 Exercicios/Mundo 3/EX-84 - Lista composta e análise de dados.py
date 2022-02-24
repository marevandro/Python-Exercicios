'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
'''

#------------------------------------  minha resolução ------------------------------------------
#parte do cadastro e fim do loop
nomes = []
dados = []
listpesadas = []
listleves = []
todos = []
cadastradas = 0
while True:
    dados.append(str(input('Qual seu nome: ')).strip().capitalize())
    dados.append(float(input('Qual seu peso: ')))
    nomes.append(dados[:])
    cadastradas += 1
    dados.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
       break 

print('-'*20,'='*5,'-'*20)
print(f'A) Foram cadastradas {cadastradas} pessoas')
print('-'*13)


#identificando quem são os pesados e leves
for peso in nomes:
    todos.append(peso[1])
pesados = max(todos)
leves = min(todos)

#validação dos pesados e leves
for pes in nomes:
    if pes[1] == pesados:
        listpesadas.append(pes[0])
    if pes[1] == leves:
        listleves.append(pes[0])
print(f'B) O maior peso foi de {listpesadas} com {pesados}Kg')
print('-'*13)
print(f'C) O menor peso foi de {listleves} com {leves}Kg')        
print('-'*20,'='*5,'-'*20)    


#-------------------------------------- resolução do curso ------------------------------------------

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp [1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}Kg',end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]',end=''}
print()