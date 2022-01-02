'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

#minha solução
comida = ("pastel","coxinha","pizza","enroladinho","sorvete")
vogais = 'a','e','i','o','u'
 
for i in comida:
    print (f'A palavra ({i}): ', end='')
    #esse for permite que eu imprima cada palavra da tupla
    
    for v in i:
    #aqui o for vai percorrer as vogais que estão na variavel
        if v.lower() in vogais:
        #se a variavel criada tiver uma vogal, ele imprime
            print(f'{v.lower()}', end='')
        
#resolução do curso
palavras = ('aprender', 'programa','linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro')
for p in palavras:
    print (f'Na palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


