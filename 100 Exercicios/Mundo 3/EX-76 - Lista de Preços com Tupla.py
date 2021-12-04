'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

#minha resolução
print ('-='*22)
print('{:^40}'.format('LISTA DE PREÇO'))
print('-='*22)

produtos = ("BALDE DE GELO",33.00,"MACERADOR",12.99,"COKTELEIRA",60.00,
    "DOSADOR",37.80,"COLHER DE BAR",16.90,"TAPETE DE BAR",37.00,"ORGANIZADOR",41.60)

for bar in range (0,len(produtos),2):
#a variavel "produto" vai ser percorrida e depois saltar o valor de 2 em 2 para ser organizado 
    print(f"{produtos[bar]:.<40}",f"R${produtos[bar+1]:>5.2f}")
#no segundo format o for percorre a variavel e adiciona mais um para mostrar somente o preço    
    
print("-=-"*16)


#resolução do curso
listagem = ('Lapis', 1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',120.32,
            'Caneta',22.30,
            'Livro',34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}' end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
