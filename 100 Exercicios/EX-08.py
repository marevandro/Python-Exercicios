'''Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.'''

metro = float(input("Quantos metros tem essa parede: "))
cent = metro * 100
mili = metro * 1000
print( "Essa parede tem {}m {:.0f}cm e {:.0f}mm".format(metro, cent, mili))
print("Agora {}m vale {}km \n"
      "Em hectómetro é igual a {}hm \n"
      "Em decâmetros é igual a {}dam".format(metro, metro / 1000,metro / 100, metro/10))
print("Em decimetros é igual a {}dm".format(metro * 10))