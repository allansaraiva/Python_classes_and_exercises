# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
while True:
    sleep(0.2)
    print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    [ 1 ] SOMAR.
    [ 2 ] MULTIPLICAR.
    [ 3 ] MAIOR.
    [ 4 ] NOVOS NÚMEROS.
    [ 5 ] SAIR DO PROGRAMA.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} + {valor2} é {soma}')
    elif opcao == 2:
        produto = valor1 * valor2
        print(f'O resultado de {valor1} x {valor2} é {produto}')
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'Entre {valor1} e {valor2} o maior é o {maior}')
    elif opcao == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        continue
    elif opcao == 5:
        break
    else:
        print('Opção inválida! Tente de novo.')
        continue
print('ENCERRANDO O PROGRAMA...')
sleep(0.5)
print('\nPROGRAMA ENCERRADO.')
