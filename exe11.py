#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

import math

#ENTRADA
num1 = float(input('Digite um número inteiro:'))
num2 = float(input('Digite outro número inteiro:'))
num3 = float(input('Digite um número real:'))

#PROCESSAMENTO
calc1 = (num1 * 2) + (num2 / 2)
calc2 = (num1 * 3) + num3
calc3 = num3 ** 3

#SAÍDA
print('O dobro de', num1, '+ metade de', num2, 'é igual a:', calc1)
print('O triplo de', num1, '+', num3, 'é igual a:', calc2)
print(num3, 'elevado ao cubo é igual a:', calc3)