print('Explicando a estrutura.')

tempo = int(input("Quantos anos tem seu carro? "))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('-'*6,'Fim','-'*6)

#condição simplificada
tempo2 = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo2 <3 else 'carro velho')
print('-'*6,'FIM','-'*6)

#Exemplo 1:
nome = str(input('Qual é seu nome? ')).strip()
if nome.lower() == 'eren':
    print('Que nome lindo você tem!')
else:
    print(f'Bom dia, {nome.capitalize()}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('Estude mais!')
