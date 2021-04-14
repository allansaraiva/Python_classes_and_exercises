# Faça um programa que converta um temperatura digitando em graus Celcius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}°C coresponde a {}°F.'.format(c, f))
