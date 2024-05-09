#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#que a tinta é vendida em latas de 18 litros que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a) comprar apenas latas de 18 litros;
# b) comprar apenas galões de 3,6 litros;
# c) misturar latas e galões, de forma que o preço seja o menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

#ENTRADA
area = float(input('Digite a área em M² a ser pintada:'))
cobertura = 6
valorgalao = 25
valorlata = 80
litrogalao = 3.6
litrolata = 18

#PROCESSAMENTO
litronecessarios = area/cobertura * 1.1
litronecessario = math.ceil(litronecessarios)
print('Serão necessários', litronecessario, 'litros para cobrir a área desejada.')

#LETRA A
qnt_lata = (litronecessario/litrolata)
valorlatas = math.ceil(qnt_lata) * valorlata
print('Serão necessárias', math.ceil(qnt_lata), 'latas e o custo total será de: R$', valorlatas)

#LETRA B
qnt_galao = (litronecessario/litrogalao)
valorgaloes = math.ceil(qnt_galao) * valorgalao
print('Serão necessários', math.ceil(qnt_galao), 'galões e o custo total será de R$:', valorgaloes)

#LETRA C
if litronecessario > (litrogalao*3):
    qtdlata = litronecessario/litrolata
    litro_resto = litronecessario % litrolata
    qtdgalaoresto = litro_resto / litrogalao
    preco_pago = (math.floor(qtdlata) * valorlata) + (math.ceil(qtdgalaoresto) * valorgalao)
    print('Visando menor valor, é recomendado comprar', math.floor(qtdlata), 'latas e', math.ceil(qtdgalaoresto), 'galões de tinta, pelo total de R$:', preco_pago)

else:
    qtdgalao = litronecessario/litrogalao
    preçopagogalao = math.ceil(qtdgalao) * valorgalao
    print('Visando menor valor, é recomendado comprar:', math.ceil(qtdgalao), 'galões de tinta, pelo total de R$:', preco_pago)