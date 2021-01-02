''' Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit.'''

celsius = float(input("Qual a temperatura em em °C: "))
converter = 32 + (celsius*1.8)
#ou
converter2 = 9 * celsius / 5+32
print("{}°C é equivalente a {:.1f}°F".format(celsius, converter))
print("Ou  {:.2f}°F".format(converter2))