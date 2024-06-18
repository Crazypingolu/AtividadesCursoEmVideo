'''
 - Programa: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
 - No final, mostre os 10 primeiros termos dessa progressão.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
primeiro = int
razao = int
decimo = int
# Entrada de dados:
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + 10 * razao
# Saída de dados:
for c in range(primeiro, decimo, razao):
    print(c)
