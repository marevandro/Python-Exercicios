''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

#minha resolução
grupoA = ('Aslborg','Kiel','Montpellier','Szeged','Elverum','Vardar 1961',
		  'Meshkov Brest','PPD Zagred')

grupoB = ('Barcelona','Veszprem','Dinamo Bucuresti','Motor','PSG','Vive Kielce',
		  'Porto','Flensburg-H.')

		 
print('{:=^45}'.format(' Liga dos Campeões *'))
print('        TEMPORADA 20/21 de HANDEBOL ')
print ()
print ()
grupo = ' '
print('A temporada conta com dois grupos A e B, qual você deseja ver ?')
while grupo not in 'AB':

    
    grupo = str(input('Grupo A ou B: ')).strip().upper()
    
    if grupo == 'A':
        print('GRUPO A SELECIONADO: ')
		#A) OS 5 PRIMEIROS TIMES.
		print()
		print(f'Os 5 primeiros times são {grupoA[0:5]}')
		#B) OS ÚLTIMOS 4 COLOCADOS.
		print(f'Os últimos 4 times na zona de rebaixamento são {grupoA[-4:]}')
		print()
		#C) TIMES EM ORDEM ALFABÉTICA.
		print(f'Sequência de times em ordem alfabética: {sorted(grupoA)}')
		print()
		#D) EM QUE POSIÇÃO ESTÁ O TIME DA Kiel
		print(f'O time Kiel esta na °{grupoA.index("Kiel")+1} posição' ) 
		print()
		#USANDO O METODO 'INDEX' ELE MOSTRA EXATAMENTE A POSIÇÃO DO INDICE, ADICIONAR '+1' FICA LEGIVEL PARA O USUÁRIO
		
		
    elif grupo == 'B':
        print('GRUPO B SELECIONADO: ')
		#A) OS 5 PRIMEIROS TIMES.	 
		print(f'Os 5 primeiros times são {grupoB[0:5]}')
		#B) OS ÚLTIMOS 4 COLOCADOS.
		print(f'Os últimos 4 times na zona de rebaixamento são {grupoB[-4:]}')
		#C) TIMES EM ORDEM ALFABÉTICA.
		print(f'Sequência de times em ordem alfabética: {sorted(grupoB)}')
		#D) EM QUE POSIÇÃO ESTÁ O TIME DA Barcelona
		print(f'O time Kiel esta na °{grupoB.index("Barcelona")+1} posição' )
		
    else:
        print('Tente novamente')



