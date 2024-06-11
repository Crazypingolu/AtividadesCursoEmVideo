'''
 - Programa: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais, um diferente
 - ESCALENO: todos os lados diferentes
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
lado01 = int
lado02 = int
lado03 = int
# Entrada de dados:
lado01 = float(input('Digite o valor da primeira reta: '))
lado02 = float(input('Digite o valor da segunda reta: '))
lado03 = float(input('Digite o valor da terceira reta: '))
# Saída de dados:
if lado01 < lado02 + lado03 and lado02 < lado01 + lado03 and lado03 < lado01 + lado02:
    if lado01 == lado02 == lado03:
        print('Um triângulo [ EQUILÁTERO ] foi formado.')
    elif lado01 == lado02 != lado03 or lado01 == lado03 != lado02 or lado03 == lado02 != lado01:
        print('Um triângulo [ ISÓSCELES ] foi formado. ')
    elif lado01 != lado02 != lado03:
        print('Um triângulo [ ESCALENO ] foi formado. ')
else:
    print('Não foi possível formar um triângulo.')
# FIM.