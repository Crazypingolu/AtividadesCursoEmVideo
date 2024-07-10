'''
 - Programa: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
 - Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
from random import randint
# Definir variáveis:
nums = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
# Saída de dados:
print("Números sorteados: ", end='')
for n in nums:
    print(n, end=" ")
print(f'\nMaior valor: {max(nums)}')
print(f'Menor valor: {min(nums)}')
# Fim.