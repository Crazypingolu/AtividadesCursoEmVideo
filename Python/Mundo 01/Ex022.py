'''
 - Programa: Crie um programa que leia o nome completo de uma pessoa e mostre: 
 - O nome com todas as letras maiúsculas e minúsculas.
 - Quantas letras ao todo (sem considerar espaços).
 - Quantas letras tem o primeiro nome.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
nome = str
nome = input('Digite seu nome: ').strip()
# Processamento + saída dados::
print('Seu nome totalmente maiúsculo é: {}'.format(nome.upper()))
print('Seu nome totalmente minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} caracteres.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
## para mostrar o primeiro nome: separa = nome.split() print separa[0] ## 
# Fim.