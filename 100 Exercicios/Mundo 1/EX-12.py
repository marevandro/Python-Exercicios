'''Faça um algoritimo que leia o preço de um produto
e mostre seu novo preço, com % de desconto.'''
preco = float(input("Quanto custa o produto? R$ "))
desconto = preco - (preco*5/100)
print("O produto que custava R${}, na promoção com desconto de 5% vai sair por R${:.2f}".format(preco, desconto))