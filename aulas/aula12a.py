nome = str(input('Qual o seu nome? ')).lower()
if nome == 'allan':
    print(f'Que nome bonito você tem, {nome}! ')

elif nome == 'pedro' or nome == 'roger' or nome == 'kaline':
    print(f'Seu nome é bem popular no brasil, {nome}!')

elif nome in 'ana  maria':
    print(f'Seu nome é bem normal, {nome}!')

else:
    print(f'Tenha um bom dia, {nome}!')
