#  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(f'No seu nome tem Silva? {"silva" in nome.lower()}')
