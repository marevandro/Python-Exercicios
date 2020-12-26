'''Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos Dólares ela pode comprar.
'''
#OBS: Considere o valor do dólar atual.


real = float(input("Quantos reais você tem na carteira: "))
dolar = real / 5.22
print("Com R${} voce consegue compra ${}".format(real, dolar))