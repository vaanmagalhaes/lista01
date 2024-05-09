#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que: #são descontados 11% para o Imposto de Renda
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto
# b) desconto INSS
# c) desconto sindicato
# d) salário líquido
# e) desconto 
# calcule os descontos e o salário líquido, conforme a tabela abaixo:+ Salário Bruto : R$, - IR (11%) : R$, - INSS (8%) : R$,  Sindicato ( 5%) : R$ = Salário Liquido : R$
import math

#ENTRADA
valor_hora = float(input('Digite quanto você ganha por hora:'))
horastrab = float(input('Digite quantas horas você trabalhou este mês:'))

#PROCESSAMENTO
salariobruto = valor_hora * horastrab
IR = salariobruto * (11 / 100)
INSS = salariobruto * (8 / 100)
SIND = salariobruto * ( 5 / 100)
descontos = IR + INSS + SIND
salarioliquido = salariobruto - descontos

#SAÍDA
print('Seu salário mensal é igual a R$:', salariobruto)
print('O valor pago ao INSS foi de R$:', INSS)
print('O valor pago ao Sindicato foi de R$:', SIND)
print('O valor pago em Imposto de Renda foi R$:', IR)
print('O total de descontos é de R$:', descontos)
print('O seu salário líquido mensal é de R$:', salarioliquido)
