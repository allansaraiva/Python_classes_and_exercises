# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso.
#
# – Entre 18,5 e 25: Peso Ideal.
#
# – 25 até 30: Sobrepeso.
#
# – 30 até 40: Obesidade.
#
# – Acima de 40: Obesidade Mórbida.

peso = float(input('Seu peso (kg): '))
altura = float(input('Altura (metro e cm): '))
imc = peso / altura ** 2
print(f'O IMC é de {imc :.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso ideal.')

elif 18.5 <= imc < 25:
    print('você está no peso ideal.')

elif 25 <= imc < 30:
    print('Você está SOBREPESO.')

elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')

else:
    print('você está com OBESIDADE MÓRBIDA.')
