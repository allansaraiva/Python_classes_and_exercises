# Escreva um programa que leia um valor em metros e o exiba convertido em Centímetros e Milímetros.
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m corresponde a \n{cm :.0f}cm \n{mm :.0f}mm ')
