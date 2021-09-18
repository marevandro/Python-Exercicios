''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''



grupoA = ('Aslborg','Kiel','Montpellier','Szeged','Elverum','Vardar 1961',
		  'Meshkov Brest','PPD Zagred')

grupoB = ('Barcelona','Veszprem','Dinamo Bucuresti','Motor','PSG','Vive Kielce',
		  'Porto','Flensburg-H.')

		 
print('{:=^45}'.format(' Liga dos Campeões *'))
print('        TEMPORADA 20/21 de HANDEBOL ')

grupo = ' '
while grupo not in 'AB':

    print('A temporada conta com dois grupos, qual você deseja ver ?')
    grupo = str(input('Grupo A ou B: ')).strip().upper()
    
    if grupo == 'A':
        print('GRUPO A SELECIONADO: ')
		#A) OS 5 PRIMEIROS TIMES.	 
		print(f'Os 5 primeiros times são {grupoA[0:5]}')
		#B) OS ÚLTIMOS 4 COLOCADOS.
		print(f'Os últimos 4 times na zona de rebaixamento são {grupoA[-4:]}')
		#C) TIMES EM ORDEM ALFABÉTICA.
		print(f'Sequência de times em ordem alfabética: {sorted(grupoA)}')
		#D) O TIME QUE VOCÊ DESEJA ESTA EM QUAL POSIÇÃO
		
		
		#TENTAR ACESSAR A POSIÇÃO DO TIME
		
		
		pesquisa = str(input('Digite o nome do time que deseja ver a posição: ')).strip().upper()
		for posi in range(0, len(grupoA)):
			print(f'O {grupoA[posi]} esta na posição {posi}')
		print(f'
		
		
		
    elif grupo == 'B':
        print('GRUPO B SELECIONADO: ')
		#A) OS 5 PRIMEIROS TIMES.	 
		print(f'Os 5 primeiros times são {grupoB[0:5]}')
		#B) OS ÚLTIMOS 4 COLOCADOS.
		print(f'Os últimos 4 times na zona de rebaixamento são {grupoB[-4:]}')
		#C) TIMES EM ORDEM ALFABÉTICA.
		print(f'Sequência de times em ordem alfabética: {sorted(grupoB)}')
    else:
        print('Tente novamente')



