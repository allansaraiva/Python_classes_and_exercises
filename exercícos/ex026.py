#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
#  em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {frase.count("a")} vezes na frase.')
print(f'A letra A apareceu pela primeira vez na posição {frase.find("a") + 1}')
print(f'A letra A aparece pela última vez na posição {frase.rfind("a") + 1}')

