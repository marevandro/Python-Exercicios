'''Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.'''

metro = float(input("Quantos metros tem essa parede: "))
cent = metro * 100
mili = metro * 1000
print( "Essa parede tem {}m {}cm e {}mm".format(metro, cent, mili))