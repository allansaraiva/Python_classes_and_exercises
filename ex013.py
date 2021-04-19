# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario :.2f}, com o aumento de 15% passará a ganhar R${novo}.')
