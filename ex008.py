# Escreva um programa que leia um valor em metros e o exiba convertido em Centímetros e Milímetros.
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a \n{:.0f}cm \n{:.0f}mm '.format(medida, cm, mm))
