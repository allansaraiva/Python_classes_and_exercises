# Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'. Caso esteja errado
# Peça digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'M, F, MASCULINO, FEMININO':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
