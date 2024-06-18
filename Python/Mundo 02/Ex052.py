'''
 - Programa: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
num = int
cont = 0
# Entrada de dados:
num = int(input("\nDigite um número: "))
# Processamento e dados:
for cto in range(1, (num + 1), 1):
    if num % cto == 0:
        print(f"\033[0;33;40m{cto}\033[m", end=" ")
        cont += 1
    else:
        print(f"\033[0;31;40m{cto}\033[m", end=" ")
    # Fim-se
# Saída de dados:
print(f"\nO número {num} foi dividido {cont} vezes")
if cont == 2:
    print("É PRIMO!")
else:
    print("Não é primo.")
# Fim.