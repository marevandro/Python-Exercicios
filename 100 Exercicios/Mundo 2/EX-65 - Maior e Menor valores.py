'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e 
qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

cont = num = continuar = soma = media = maior = menor = 0
print('-'*6,'Maior e Menor valor','-'*6)
while continuar != 2:
    num = int(input('Digite um valor: '))
    continuar = int(input('''Você deseja continuar ? 
[ 1 ] para SIM e [ 2 ] para NÃO: '''))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num              
media = soma / 2
print(f'A média entre os números é {media}, o total da soma entre os números é {soma}')
print (f'O maior número digitado é {maior} e o menor é {menor}')

#resoluçõa do curso

#resp = 'S'
#soma = quant = média = maior = menor = 0
#while resp in 'Ss':
  #  núm = int(input('Digite um número: '))
   # soma += núm
   # quant += 1
   # if quant == 1:
    #    maior = menor = núm
   # else: 
   #     if núm > maior:
   #         maior = núm
   #     if núm < menor:
   #         menor = núm
    #resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
     #lembrnado, upper joga pra maiusculo, strip elimina os espaços e [] considera a primeira str
#média = soma / quant
#print('Você digitou {} números e a média foi {}'.format(quant, média))
#print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))
