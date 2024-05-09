#Tendo como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
import math

#ENTRADA
print('Vamos calcular o seu peso ideal:')
alt = float(input('Qual a sua altura?'))

#PROCESSAMENTO
pidealh = (72.7 * alt) - 58
pidealm = (62.1 * alt) - 44.7

#SAÍDA
print('Sendo mulher, seu peso ideal é:', math.ceil(pidealm), 'kgs')
print('Sendo homem, seu peso ideal é:', math.ceil(pidealh), 'kgs')
