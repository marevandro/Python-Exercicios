''' Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.'''
#resolução do curso, não consegue fazer sozinho
maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg.')
print(f'O menor peso lido foi de {menor}kg.')

#Aqui vou deixar uma explicação para compreensão do exercício.
'''Ele cria um IF (SE), que fica num sentido de (QUANDO O VALOR FOR DIGITADO).
Depois pega o 1° valor digitado no PESO e compara com o primeiro valor contabilizado pelo P, 
se o ° valor for igual a primeira contabilização do P {que com certeza vai ser):

Ele atribui esse valor para as variantes MAIOR e MENOR dentro do primeiro IF.

Depois, ele cria o ELSE para comparar os valores restante com o valor MAIOR e MENOR
do primeiro IF (os dois tem o mesmo valor).

Dentro do ELSE no primeiro IF, ele compara se os valores restantes é ou não maior que
o valor dentro da variante MAIOR, se for então essa variante 
passa a receber o novo valor, se não continua o mesmo valor e vai para o próximo valor restante até acabar. 


Depois, ainda dentro do ELSE no segundo IF, ele compara se os valores restantes é ou não 
menor que o valor dentro da variante MENOR, se for então essa variante passa a receber 
o novo valor, se não continua o mesmo valor e vai para o próximo valor restante até acabar. 

E no final ele mostra os novos valores atribuídos as variantes MAIOR e MENOR no PRINT.

Agradecimentos ao comentário de MikaelX, dentro do canal Curso em Vídeo no YouTube.'''



