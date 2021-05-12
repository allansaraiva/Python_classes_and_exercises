#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final mostre os 10 primeiros termos dessa progressão.

print('''
=====================================
10 TERMOS DE UMA PA
=====================================''')
termo_1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ultimo = termo_1 + (10 - 1) * razao
for c in range(termo_1, ultimo + razao, razao):
    print(c)
