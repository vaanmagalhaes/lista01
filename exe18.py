#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
import math

#ENTRADA
tam = float(input('Qual o tamanho do arquivo em MB?'))
vel = float(input('Qual a velocidade do link da internet em Mbps?'))

#PROCESSAMENTO
tempo = ((tam*8) / vel) / 60

#SAÍDA
print('O tempo de download é igual a', math.ceil(tempo), 'minutos')