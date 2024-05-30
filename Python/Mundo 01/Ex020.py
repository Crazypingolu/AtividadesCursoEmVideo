'''
 - Programa: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
 - Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Trazer biblioteca:
import random
# Declarar variáveis:
listaDeAlunos = []
# Entrada de dados:
print("")
for cto in range(0,4):
    # .append - adiciona na lista
    listaDeAlunos.append(input(f"Digite o NOME do {(cto + 1)}º aluno: "))
# Processamento de dados:
random.shuffle(listaDeAlunos)
# Saída:
print(f"\nA nova ordem de apresentação será: \n{listaDeAlunos}")
