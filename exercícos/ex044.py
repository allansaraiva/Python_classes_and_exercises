# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto.
#
# – à vista no cartão: 5% de desconto.
#
# – em até 2x no cartão: preço formal.
#
# – 3x ou mais no cartão: 20% de juros.

preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO:')
print('[ 1 ] - À vista dinheiro/cheque.')
print('[ 2 ] - À vista no cartão.')
print('[ 3 ] - 2x no cartão.')
print('[ 4 ] - 3x ou mais no cartão.')
opcao = int(input('sua opção: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)

elif opcao == 2:
    total = preco - (preco * 5 / 100)

elif opcao == 3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcela :.2f} SEM JUROS.')

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcela = int(input('Quantas parcelas? '))
    parcela = total / total_parcela
    print(f'Sua compra será parcelada em {total_parcela}x de R${parcela :.2f} COM JUROS.')

else:
    total = preco
    print('Opção inválida. Tente novamente!')

print(f'sua compra de R${preco :.2f} vai custar R${total :.2f}')
