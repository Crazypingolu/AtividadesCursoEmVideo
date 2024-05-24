'''
 - Programa: Faça um algoritmo que leia o salário de um funcionário e 
 - mostre seu novo salário, com 15% de aumento.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variávies
salOriginal = float
salReajuste = float
# Entrada de dados:
salOriginal = float(input(" \nDigite o valor do salário: "))
# Processamento de dados:
salReajuste = salOriginal * 1.15
# Saída de dados:
print(f"Salário reajustado: {salReajuste:.2f}")