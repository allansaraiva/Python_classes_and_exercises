# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
# ela pode comprar.
# Considere US$1.00 = R$5.55
real = float(input('Quanto dinheiro você tem na carteira ou no banco? R$'))
dolar = real / 5.55
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))

