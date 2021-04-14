# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la. Sabendo que cada litro de tinta pinta 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem uma dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta'.format(tinta))
