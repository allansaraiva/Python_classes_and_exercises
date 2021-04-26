# # Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-=' * 30)
escolha = randint(0, 5)
opcao = int(input('Escolha um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if opcao == escolha:
    print('PARABÉNS! você me venceu!')
else:
    print(f'GANHEI! Eu pensei no número {escolha} e não no número {opcao}')
