'''
 - Programa: Faça um programa que leia um número qualquer e mostre o seu fatorial.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
num = int
resultado = 1
cto = 1
# Entrada de dados:
print('')
num = int(input("\nDigite um número e o programa irá calcular seu fatorial: \n"))
# Processamento de dados:
while cto < (num + 1):
    resultado = resultado * cto
    cto += 1
# Saída de dados:
print(f'O fatorial de {num} é igual a: \033[32m{resultado}\033[m')
# Fim.