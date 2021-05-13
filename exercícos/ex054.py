# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
cont_maiores = 0
cont_menores = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}° pessoa: '))
    if atual - ano >= 18:
        cont_maiores += 1
    else:
        cont_menores += 1
print(f'{cont_maiores} pessoas são maiores de idade.')
print(f'{cont_menores} pessoas são menores de idade.')
