'''
 - Programa: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
numero = int
resultado = int
# Entrada de dados:
print("..."*6)
numero = int(input("Digite um número, o programa dirá se ele é par ou ímpar: "))
# Processamento de dados:
resultado = numero % 2
# Saída de dados:
if resultado == 0:
    print("O número é PAR!")
else:
    print("O número é ÍMPAR!")
# Fim