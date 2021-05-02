# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year  # PARA SABER O ANO ATUAL
nascimento = int(input('Em que ano você nasceu? '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem, ou vai fazer, {idade} anos em {atual}')

if idade == 18:
    print('\n\033[33mVocê tem que se alistar esse ano!\033[m')

elif idade < 18:
    saldo = 18 - idade
    print(f'\n\033[32mAinda faltam {saldo} anos para o seu alistamento!\033[m')
    ano = atual + saldo
    print(f'\033[32mSeu alistamento será em {ano}!\033[m')

else:
    saldo = idade - 18
    print(f'\n\033[31mVocê deveria ter se alistado há {saldo} anos!\033[m')
    ano = atual - saldo
    print(f'\033[31mSeu alistamento foi em {ano}\033[m')
