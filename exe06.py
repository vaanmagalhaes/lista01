#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

print('Descubra a área de círculo através do raio')
area = float(input('Digite o raio do círculo:'))
result = math.pi * (area ** 2)

print('A área do círculo é equivalente a:', result)