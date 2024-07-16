'''
 - Programa: Crie um programa que vai ler vários números e colocar em uma lista. 
 - Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
 - Ao final, mostre o conteúdo das três listas geradas.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
lista = []
resp = str
par = []
impar = []
# Entrada de dados:
print(' ')
while True:
    lista.append(int(input("Digite um número: ")))
    resp = input("Continuar? \n[s]/[n]: ")
    if resp in "Nn":
        break
# Processamento de dados:
for i, v in enumerate(lista):
    if i % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
# Saída de dados:
print("Lista completa: ", *lista)
print("Pares: ", *par)
print("Ímpares: ", *impar)
# Fim.