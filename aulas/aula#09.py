frase = ('FAla tu que eu to cansado!')
print(frase.lower()[::2])#diminui as str
print(frase.upper())#aumenta as str
print(frase.count('o'))#conta quantas unidades entre as aspas tem
print(len(frase)) #conta quantas str
print(frase.replace('FAla','Diga ai,'))#so substitui e não salva
#para salvar tem que desgnar isso na variavel.
print('Cuso' in frase) #True ou false se a str estiver na variavel
print(frase.find('tu')) #mostra em qual posição começa
print(frase.find('TU')) #-1 caso não tenha
print(frase.upper().find('TU')) #agora pq deixei em maiusculo como na pesquisa
print(frase.split())
partes = frase.split()
print(partes[2][1]) #nesse caso ele não conta um antes