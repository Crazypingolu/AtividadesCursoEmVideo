'''
 - Programa: Escreva um programa que leia dois números inteiros e compare-os. 
 - mostrando na tela uma mensagem:
 - O primeiro valor é maior
 - O segundo valor é maior
 - Não existe valor maior, os dois são iguais
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
num1 = int
num2 = int
# Entrada de dados:
print("")
num1 = int(input("Digite o 1º NÚMERO: "))
num2 = int(input("Digite o 2º NÚMERO: "))
# Saída:
if num1 > num2:
    print("1º número é maior.")
elif num2 > num1:
    print("2º número é maior.")
else:
    print("Ambos são iguais.")
# Fim