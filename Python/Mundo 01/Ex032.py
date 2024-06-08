'''
 - Programa: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from datetime import date
# Definir variáveis:
ano = int
bisexto = bool
# Entrada de dados:
ano = int(input('''
Digite o ano para o programa análisar se é bisexto (0 = ano atual): 
'''))
# Processamento de dados:
if ano == 0: # Define o ano atual
    ano = date.today().year
# fim-se
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Fórmula do ano bisexto.
    bisexto = True
else:
    bisexto = False
# Saída de dados:
if bisexto == True:
    print("O ano É BISEXTO!")
else:
    print("O ano NÃO É BISEXTO!")
# Fim.