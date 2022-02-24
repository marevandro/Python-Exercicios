'''Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

#------------------------------- minha resolução ----------------------------------------

#entrada de valores
num = []
par = []
impar = []
valores = 0 #criei essa variavel tipo int pois na ocasião eu não consegui usar os operadores logicos se não fosse um int
for i in range(0,7):
   num.append(int(input('Digite um numero: ')))
print('-'*20,f'Resultado','-'*20)

#par ou impar
for i in num:
    valores = int(i)
    if valores % 2 ==0:
        par.append(valores)
        par.sort()        
    else:
        impar.append(valores)
        impar.sort()
print(f'Os valores par em onrdem crescente são: {par}')
print('-'*5)
print(f'Os valores impares em ordem crescente são: {impar}')
print('-'*5)

#------------------------------- resolução do curso ----------------------------------------

núm = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input('Digite o {c}°. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]'}
        
