#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
import math

fare = float(input('Digite a temperatura em Farenheit:'))
calc = 5 * (fare-32) / 9

print(fare, 'Farenheit é igual a ', calc, 'Celsius')