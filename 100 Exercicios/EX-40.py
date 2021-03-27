'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

#minha resolução
from time import sleep
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
pontos = 7.0 - media
print('Estamos verificando o seu resultado...')
sleep(3)
if media < 5:
    print('REPROVADO!')
    print(f'Sua média foi {media:.1f}, até proximo ano.')
elif media >= 5 and media <= 6.9:
#elif 5 > media >=6.9: outra maneira de conduziar essa comparação no python
    print('RECUPERAÇÃO!')
    print(f'Sua média foi {media:.1f}, você precisa de {pontos:.1f} para passar por média.')
elif media >= 7:
    print('APROVADO!')
    print(f'Meus parabéns por sua média foi, {media:.1f}!')

#resolução do curso, muito parecida com a resolução que criei
