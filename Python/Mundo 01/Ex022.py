nome = str(input('Digite seu nome: ')).strip()
print('Seu nome totalmente maiúsculo é: {}'.format(nome.upper()))
print('Seu nome totalmente minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} caracteres.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

## para mostrar o primeiro nome: separa = nome.split() print separa[0] ## 
