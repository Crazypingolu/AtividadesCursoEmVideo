'''
 - Programa: Crie um programa que leia o nome de uma pessoa e diga silva ela tem "SILVA" no nome.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
nome = str
silva = bool
# Entrada de dados:
nome = input('Digite um NOME (completo): ').strip().upper()
# Processamento de dados:
silva = 'SILVA' in nome
# Saída de dados:
print('O nome digitado tem silva? [{}]'.format(silva))
# Fim