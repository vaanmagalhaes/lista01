#Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

#ENTRADA
area = float(input('Digite a área a ser pintada em M²:'))
litrolata = 18
cobertura = 3
valorlata = 80

#PROCESSAMENTO
litronecessario = area/cobertura
qtd = litronecessario/litrolata
valortotal = math.ceil(qtd) * valorlata

#SAÍDA
print('Para pintar', area, 'M² será necessário usar', math.ceil(qtd), 'latas de tinta e o preço total a ser pago é:', valortotal)