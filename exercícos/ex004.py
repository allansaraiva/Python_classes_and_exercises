# Faça um program que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas a informações possíveis sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo de "{}" é'.format(a), type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está eu minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())
