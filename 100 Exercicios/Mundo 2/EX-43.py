'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

#minha resolução
from time import sleep
peso = float(input('Seu peso atual: '))
altura = float(input('Sua altura atual: '))
print('Vamos calcular o seu IMC (Índice de Massa Corporal).')
sleep (3)
IMC = peso / (altura**2)
if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.1f}kg/m, por isso você está ABAIXO DO PESO.')
elif 18.5 <= IMC <=25:
    print(f'Seu IMC é de {IMC:.1f}kg/m, você está no PESO IDEAL!')
elif 25 <= IMC <=30:
    print(f'Seu IMC é de {IMC:.1f}kg/m, você esta com SOBREPESO, vamos se cuidar.')
elif 30 <= IMC <= 40:
    print(f'Seu IMC é de {IMC:.2f}kg/m, cuidado você esta com OBESIDADE.')
else:
    print(f'{IMC:.1f}, procure um médico! Você esta com OBESIDADE MÓRBIDA.')



#fiz básicamente a mesma resolução do curso
