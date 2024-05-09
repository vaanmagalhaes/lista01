#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
import math

print('Calcule seu salário mensal:')
din = float(input('Diga quanto você ganha por hora:'))
hrs = float(input('Diga quantas horas você trabalha por mês:'))
sal = din * hrs

print('Seu salário mensal é igual a R$',sal)