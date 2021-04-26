# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
limite = 80
multa = (velocidade - limite) * 7
if velocidade <= limite:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite máximo que é 80Km/h')
    print(f'Você terá que pagar uma multa de R${multa :.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')
