# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la. Sabendo que cada litro de tinta pinta 2m².

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem uma dimensão de {larg :.2f}x{alt :.2f} e sua área é de {area :.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta :.2f}L de tinta')
