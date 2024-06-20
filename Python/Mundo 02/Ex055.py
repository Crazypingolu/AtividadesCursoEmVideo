'''
 - Programa: Faça um programa que leia o peso de cinco pessoas. 
 - No final, mostre qual foi o maior e o menor peso lidos.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Denifir variáveis:
peso = int
pesoMaior = 0
pesoMenor = 0
# Entrada de dados:
print("")
for cto in range(0,5,1):
    peso = int(input(f"Digite o peso da {(cto + 1)}º pessoa: \n"))
# Processamento de dados (DENTRO DO FOR):
    if pesoMaior == 0:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if pesoMaior < peso:
            pesoMaior = peso
        if pesoMenor > peso:
            pesoMenor = peso
# Saída de dados:
print(f"Maior peso: \033[1;31m{pesoMaior}\033[m")
print(f"Menor peso: \033[1;33m{pesoMenor}\033[m")
# Fim.