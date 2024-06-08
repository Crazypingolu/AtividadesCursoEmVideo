'''
 - Programa: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 - Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
salario = float
reajuste = float
# Entrada de dados:
salario = float(input("\nDigite o SALÁRIO: "))
# Processamento de dados:
if salario > 1250:
    reajuste = salario * 1.1
else: 
    reajuste = salario * 1.15
# Saída de dados:
print(f"Salário reajustado: R${reajuste:.2f}")
# Fim.