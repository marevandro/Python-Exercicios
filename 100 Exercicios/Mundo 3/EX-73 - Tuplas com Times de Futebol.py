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
print ()
print ()
grupo = ' '
print('A temporada conta com dois grupos A e B, qual você deseja ver ?')
while grupo not in 'AB':

    
    grupo = str(input('Grupo A ou B: ')).strip().upper()
    
    if grupo == 'A':
        print('Grupo A selecionado: ')
		#A) OS 5 PRIMEIROS TIMES.
		print()
		print(f'Os 5 primeiros times do grupo A são: {grupoA[0:5]}')
		#B) OS ÚLTIMOS 4 COLOCADOS.
		print(f'Os últimos 4 times do grupo A são: {grupoA[-4:]}')
		print()
		#C) TIMES EM ORDEM ALFABÉTICA.
		print(f'Sequência de times em ordem alfabética: {sorted(grupoA)}')
		print()
		#D) EM QUE POSIÇÃO ESTÁ O TIME DA Kiel
		print(f'O time Kiel esta na {grupoA.index("Kiel")+1}ª posição' ) 
		print()
		#USANDO O METODO 'INDEX' ELE MOSTRA EXATAMENTE A POSIÇÃO DO INDICE, ADICIONAR '+1' FICA LEGIVEL PARA O USUÁRIO
		
		
    elif grupo == 'B':
        print('Grupo B selecionado: ')
		#A) OS 5 PRIMEIROS TIMES.	 
		print(f'Os 5 primeiros times do grupo B são: {grupoB[0:5]}')
		#B) OS ÚLTIMOS 4 COLOCADOS.
		print(f'Os últimos 4 times do grupo B são: {grupoB[-4:]}')
		#C) TIMES EM ORDEM ALFABÉTICA.
		print(f'Sequência de times em ordem alfabética: {sorted(grupoB)}')
		#D) EM QUE POSIÇÃO ESTÁ O TIME DA Barcelona
		print(f'O time Barcelona esta na {grupoB.index("Barcelona")+1}ª posição' )
		
    else:
        print('Tente novamente')
print('-'*20)

#resolução do curso


times = ('Corinthians','Palmeiras','Santos','Grêmio',
		 'Cruzeiro','Flamengo','Vasco','Chapecoense',
		 'Atlético','Botafogo','Atlético-PR','Bahia',
		 'São Paulo','Fluminense','Sport Recife',
		 'EC Vitória','Coritiba','Avaí','Ponte Preta',
		 'Atlético-GO')

print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")}ª posição')
