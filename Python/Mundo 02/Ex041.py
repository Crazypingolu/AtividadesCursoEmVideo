'''
 - Programa:  A Confederação Nacional de Natação precisa de um programa que leia o 
 ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
 - Até 9 anos: MIRIM
 - Até 14 anos: INFANTIL
 - Até 19 anos: JÚNIOR
 - Até 25 anos: SÊNIOR
 - Acima de 25 anos: MASTER
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca
from datetime import date
# Definir variáveis:
nascimento = int
idade = int
data = date.today().year
# Entrada de dados:
nascimento = int(input("Digite a idade: "))
# Processamento de dados:
idade = data - nascimento
# Saída de dados:
if idade <= 9:
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('Categoria: JUNIOR.')
elif idade <= 20:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')
