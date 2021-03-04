'''Desenvolva um programa que pergunte a distância de
uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 para viagens mais longas.
'''
#minha resolução
km = float(input('Qual a distancia que você percorreu? '))
if km <= 200:
    passagem = km * 0.50 #se a condição cair aqui, esse vai ser o valor da variavel
else:
    passagem = km * 0.45#aqui segue a mesma logica, por isso não colocar um 'print' em cada condição
print(f'Você rodou {km:.2f}km, sua viagem custa R$ {passagem:.2f}')
print('-'*10,'FIM','-'*10)
#resolução do curso

#resolução 1:
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

#resolução 2
distancia2 = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia2))
preço2 = distancia2 * 0.50 if distancia2 <= 200 else distancia2 * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço2))