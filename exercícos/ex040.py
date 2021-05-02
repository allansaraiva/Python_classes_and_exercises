# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
# de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
med = (nota1 + nota2) / 2

if med < 5.0:
    print(f'\n\033[31mSua média foi {med :.1f}, você está REPROVADO!\033[m')

elif 7 > med >= 5.0:
    print(f'\n\033[33mSua média foi {med :.1f}, você está de RECUPERAÇÃO!\033[m')

else:
    print(f'\n\033[32mSua média foi {med :.1f}, você está APROVADO!\033[m')
