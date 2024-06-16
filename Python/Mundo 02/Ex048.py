'''
 - Programa: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
soma = int
# Entrada de dados:
soma = 0
# Processamento de dados:
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
    # Fim - Se
# Fim - for
# Saída de dados:
print(f"A Soma de todos os números multiplos de 3 é: {soma}")
# Fim.