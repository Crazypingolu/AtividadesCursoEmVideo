'''
 - Programa: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
from math import trunc
x =  float(input('Digite um valor: '))
y = trunc(x)
print('a porção inteira do número {} é {}'.format(x, y))