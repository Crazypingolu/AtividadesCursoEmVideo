'''
 - Programa: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
cidade = str
santo = bool
# Entrada de dados:
cidade = input('\nDigite o nome da cidade: ').strip().upper()
# Processamento de dados:
santo = cidade[:5] == 'SANTO'
# Saída de dados:
print('A cidade tem santo em seu nome? [{}]'.format(santo))
# Fim