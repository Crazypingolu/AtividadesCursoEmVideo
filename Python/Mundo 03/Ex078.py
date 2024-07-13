'''
 - Programa: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 - No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
lista = list()
maior = -1
mal = 0
menor = int
mel = 0
# Entrada de dados:
print(' ')
for c in range(0,5,1):
    lista.append(int(input(f"Digite {c + 1}º número: ")))
    if maior == -1:
        maior = lista[c]
        menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
            mal = c
        elif menor > lista[c]:
            menor = lista[c]
            mel = c
# Saída de dados:
print(f'O maior número é: {maior} e seu índice é: {mal}')
print(f'O maior número é: {menor} e seu índice é: {mel}')
# Fim.