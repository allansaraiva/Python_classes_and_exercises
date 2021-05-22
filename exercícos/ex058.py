# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
print('-=' * 30)
escolha = randint(0, 5)
palpite = 0
acertou = False
while not acertou:
    opcao = int(input('Escolha um núemro entre 0 e 5: '))
    palpite += 1
    if opcao == escolha:
        acertou = True
    else:
        if opcao < escolha:
            print('Mais... Tente de novo.')
        elif opcao > escolha:
            print('Menos... Tente de novo.')
print(f'PARABÉNS! Eu pensei no número {escolha} e você precisou de {palpite} tentativas para acertar.')
