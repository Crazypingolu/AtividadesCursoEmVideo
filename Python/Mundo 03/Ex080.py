'''
 - Programa: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
 - já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. 
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
lista = []
num = int
cont = int
# Entrada de dados:
print(' ')
for n in range(0,5,1):
    num = int(input(f"Digite o {n+1}º número: "))
    if n == 0 or num > lista[-1]:
        lista.append(num)
    else:
        cont = 0
        while cont < len(lista):
            if num <= lista[cont]:
                lista.insert(cont, num)
                break
            cont += 1
# Saída de dados:
print("Lista dos números digitados em ordem crescente: \n", *lista)
# Fim.