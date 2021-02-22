'''Crie um programa que leia o nome de uma cidade diga se
ela começa ou não com o nome “SANTO'''

#Minha resolução
entendi = input('''Aqui vamos encontrar a palavra "santos" em qualquer posição dentro da variavel.
Aperte qualquer botão para continuar: ''')
cidade = str(input('Qual o nome da sua cidade: ')).strip()
santo = cidade.upper()
print ('CAUCAIA' in santo)

#Resolção do curso
entendi = input('''Nessa resolução a leitura é feita apenas de 0 á 5.
Aperte qualquer botão para continuar: ''')
cid = str(input('Em qual cidade você nasceu ? ')).strip()
print(cid[0:5].upper() == 'SANTO')

