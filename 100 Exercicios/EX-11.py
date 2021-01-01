'''Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2m².'''

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
metros = largura * altura
tinta = metros / 2
print("Para consguirmos pintar uma parede de {:.2f}m² precisamos de {:.1f} litros de tinta".format(metros, tinta))