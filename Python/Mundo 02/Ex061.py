'''
 - Programa: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
 - mostrando os 10 primeiros termos da progressão usando a estrutura while.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from time import sleep
# Definir variáveis:
termo1 = int
razao = int
resultado = int
cto = 0
# Entrada de dados:
print(" ")
termo1 = int(input("\nDigite o 1º termo da PA: \n"))
razao = int(input("Digite qual a razão da PA: \n"))
# Processamento de dados:
resultado = termo1
print(f"\nOs 10 termos da PA com primeiro termo {termo1} e razão de {razao} é:")
while cto < 10:
    print(f'{resultado}', end=" ")
    resultado += razao
    cto += 1
sleep(1)
print("\n\n{:-^40}".format(" Fim "))
sleep(0.5)
# Fim.