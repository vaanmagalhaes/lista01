#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
import math

cel = float(input('Digite a temperatura em Celsius:'))
fare = cel * 1.8 + 32

print(cel, 'Celsius é igual a', fare, 'Farenheit')