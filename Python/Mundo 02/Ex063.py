'''
 - Programa: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
# Definir variáveis:
cto = int
termo1 = 0
termo2 = 1
total = 0
quant = int
# Entrada de dados:
print(" ")
quant = int(input("Digite até quantos elementos de fibonacci o programa deve mostrar: \n"))
# Processamento de dados:
print(f'\n\033[1;33m{termo1}\033[m', end=" ")
cto = 2
while cto <= quant:
    total = termo1 + termo2
    print(f'\033[1;33m{total}\033[m', end=" ")
    termo2 = termo1
    termo1 = total
    cto += 1
# Fim.