#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
import math

#ENTRADA
print('Vamos calcular o seu peso ideal:')
alt = float(input('Qual a sua altura?'))

#PROCESSAMENTO
pideal = (72.7 * alt) - 58

#SAÍDA
print('Seu peso ideal é:', math.ceil(pideal), 'kgs')
