'''Aula 18:

Sempre que eu desejar mudar a segunda estrutura da lista, preciso criar uma copia '[:]'
'''


'''teste = list ()
teste.append('Marcio')
teste.append(26)
galera = list ()
galera.append (teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Beatriz',22],['Monique',18],['Isadora',12],['Miguel',7]]
print(galera[2][1])
print('-'*15)'''
#fazendo uma lista
'''for p in galera:
    print(p)
#para ('p') cada pessoa em (in) galera (variavel) mostre uma lista
print('-'*15)'''
#interação do format na lista
'''for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

#interação com o usuário, usando input
#1° variavel, vai ser a principal
galera = []
#2° variavel, vai ser apenas para receber os primeiros dados
dado = []
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    #atenção nessa parte, o dado recebeu a informação, mas vai repassar para
    #a var principal, por isso precisa ser uma copia
    galera.append(dado[:])
    dado.clear()
print(galera)

#para mostrar dados mais especificos, que so mostre os maiores de idade
for p in galera:
    if p[1] >= 18:
      print(f'{p[0]} é maior de idade.')
      totmai += 1
    else:
      print(f'{p[0]} é menor de idade.')
      totmen += 1
print(f'Temos {totmai} maiores e {totmen} menor de idade.')