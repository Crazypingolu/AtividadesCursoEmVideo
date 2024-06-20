'''
 - Programa: Crie um programa que leia o ano de nascimento de sete pessoas. 
 - No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from datetime import date
# Definir variáveis:
maiorIdade = 0
menorIdade = 0
anoAtual = date.today().year
anoNascimento = int
# Entrada de dados:
print("")
for cto in range(0, 7, 1):
    anoNascimento = int(input(f"Digite a DATA DE NASCIMENTO da {(cto+1)}º pessoa:\n"))
# Processamento de dados (dentro do for):
    if(anoAtual - anoNascimento) < 18:
        maiorIdade += 1
    else:
        menorIdade += 1
# Saída de dados:
print(f"\033[1;31m{maiorIdade}x\033[m maiores de idade.")
print(f"\033[1;33m{menorIdade}x\033[m menores de idade.")
# Fim.