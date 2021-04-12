'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

#minha resolução
speed = float(input("Qual a velocidade do carro? "))
if speed >= 80.0:
    ticket = (speed - 80.0) * 7.0 #como o valor ja é estabelecido, apenas subtraimos
    print(f'Você vai ser multado! O valor da multa é R$ {ticket}')

else:
    print('Boa viagem, vai com DEUS!')
#resolção do curso
velocidade = float(input('Qual é a velocidade atual do carro ?'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f)!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')