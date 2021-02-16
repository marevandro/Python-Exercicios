frase = ('Fala tu que eu to cansado!')
print(f'A frase é: {frase}')
print('='*25)
print('Brincando com a frase.')
print('Começando na str 2 ate o final, pulando de 2 em 2')
print(frase[2::2])
print('Da str 15 ate a 26')
print(frase[15:])
print('='*25)



print('-'*25)
print('A função "len" vem de comprimento, mostra quantas str tem, incluindo os espaços. ')
print(('Quantas strings tem: '),len(frase)) #conta quantas str, espaços tbm contam
#print(len(frase))

print('-'*25)
print('Para a tradução livre count e contar, e verifica quantas vezes a str selecionada aparece.')
print(('Quantas str com a letra "a" tem: '),frase.count('a'))
print(('Quantas letras "a" existem começando da str 5 ate a 10: '), frase.count('a',5,10))
#print(frase.count('a'))

print('-'*25)
print(('Com o "find"(Encontrar), localizamos a onde a str começa: '),frase.find('tu'))
#print(frase.find('tu'))
print(('No caso de não encontrar a str, find retorna o valor "-1":'), frase.find('TU'))
#print(frase.find('TU'))
print(('Nesse ultimo caso, usando a função upper, eu equalizo a str'), frase.upper().find('TU'))
#print(frase.upper().find('TU'))

print('-'*25)
print('O operador "in" apenas informa se existe a str selecionada na variavel.')
print(('Exemplo: existe a palavra "amigo" na variavel frase ?'), 'amigo' in frase)
print('Retorna True(verdadeiro) ou False (falso).')
#print('Cuso' in frase)

print('-'*25)
print('Com o metodo "replace", eu consigo substituir a palavra nessa instância.')
print(f'Dentro da frase "{frase}", vamos substituir "Fala", por "Diga ai": ')
print(frase.replace('Fala','Diga ai,'))


print('-'*25)
print('Com a funcionalidade UPPER (Superior), eu consigo deixar as str em maiúsculo.')
print(frase.upper())
print('Com a funcionalidade lower (inferior), eu consigo deixar as str em minúsculo.')
print(frase.lower())

print('-'*25)
print('A funcionalidade "capitalize" deixa apenas a primeira str em maiúsculo.')
print(frase.capitalize())
print('A funcionalidade "title" separa as str entre os espaços\ne deixa a primeira letra maiúscula.')
print(frase.title())

print('-'*25)
print('A funcionalidade "strip", retira os espaços no inicio e fim da str (lembrando que os espaços contam na str).')
print('Usada em casos de entradas para texto a onde o usuário digita o espaço sem necessidade.')
comand = str(('          Ola mundo!       '))
print(f'Exemplo: {comand}')
print('Com strip:',comand.strip())
print('Para tirar os espaços so da direita usar "rstrip", somente os da esquerda usar "lstrip".')


print("-"*25)
print('O split cria uma divisão, a onde tiver espaço ele vai dividir.')
print(frase.split())
print('Apos dividir, posso criar uma variavel para guardar o valor (palavra) que eu quiser.')
partes = frase.split()
print('Mostre apenas a ultima palavra: ', partes[5])
print('Mostre apenas a primeira letra da ultima palavra: ',partes[5] [0])

print('-'*25)
print('Com "join", vamos fazer a junção dos espaços colocando uma str.')
print('Aqui o resultado eu ja usei uma variavel que eu tinha criado para dividir a frase.')
print('-'.join(partes))