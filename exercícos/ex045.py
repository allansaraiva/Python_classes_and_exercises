# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Escolha um item:
[ 0 ] - PEDRA.
[ 1 ] - PAPEL.
[ 2 ] - TESOURA.''')
jogador = int(input('Qual é a sua jogada? '))
print('\nJO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PÔ\n')
sleep(0.4)
print('-=' * 12)
print(f'computador jogou {itens[computador]}')
print(f'jogador jogou {itens[jogador]}')
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('JOGADOR VENCE!')

    elif jogador == 2:
        print('COMPUTADOR VENCE!')

    else:
        print('OPÇÃO INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('JOGADOR VENCE!')

    else:
        print('OPÇÃO INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')

    elif jogador == 1:
        print('COMPUTADOR VENCE!')

    elif jogador == 2:
        print('EMPATE!')

    else:
        print('OPÇÃO INVÁLIDA!')

else:
    print('OPÇÃO INVÁLIDA!')
