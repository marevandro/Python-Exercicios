'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

#minha resolução

num_exte = ('zero','um','dois','tres','quatro',
			'cinco','seis','sete','oito',
			'nove','dez','onze','doze','treze',
			'quatorze','quinze','dezesseis',
			'dezessete','dezoito','dezenove','vinte')
while True:
    num_user = int(input('Digite um número de 0 ate 20 = '))
    if 0 >= num_user <= 20:
        break
print(f'O número digitado é {num_exte[num_user]}')

#A variavel quem vai acessar a tupla
