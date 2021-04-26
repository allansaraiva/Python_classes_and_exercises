# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da sua viajem? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'Sua viajem irá custar R${preco :.2f}')
print('Boa viajem!')
