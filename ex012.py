# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5/100)
print(f'O produto que custava R${preco :.2f}, com o desconto de 5% irá custar R${novo :.2f} ')
