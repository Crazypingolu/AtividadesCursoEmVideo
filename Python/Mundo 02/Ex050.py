'''
 - Programa: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
 - Se o valor digitado for ímpar, desconsidere-o.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
num = int
soma = int
# Entrada e Processamento:
for c in range(1, 7, 1):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
    # fim - se
# Saída de dados:
print(f"A soma dos pares: {soma}")
# Fim.