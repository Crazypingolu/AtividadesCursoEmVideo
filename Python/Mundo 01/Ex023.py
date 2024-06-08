'''
 - Programa: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
num = int
quantUnidades = int
quantDezenas = int
quantCentenas = int
quantMilhares = int
# Entrada de dados:
num = int(input('Digite um número: '))
# Processamento de dados:
quantUnidades = num // 1 % 10
quantDezenas = num // 10 % 10
quantCentenas = num // 100 % 10
quantMilhares = num // 1000 % 10
# Saída de dados:
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(quantUnidades,quantDezenas,quantCentenas,quantMilhares))
# Fim.