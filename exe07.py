#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
import math

base = float(input('Digite a base de um quadrado:'))
area = base ** 2
result = area * 2

print('A área do quadrado é igual a:', area)
print('O dobro desta área é igual a:', result)