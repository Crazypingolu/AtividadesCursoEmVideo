'''
 - Programa:Crie um programa que leia vários números inteiros pelo teclado. 
 - No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
 - O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
# Definir variáveis:
num = int
media = 0
cto = 0
cont = " "
maior = 0
menor = 0
# Entrada de dados:
print(' ')
while cont != "N":
    cont = " "
    num = int(input("Digite um número: \n"))
    media += num
    cto += 1
    if maior == 0:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
    while cont == " ":
        cont = input("Quer continuar? \nDigite [S] para continuar ou [N] para terminar o programa: \n").upper().strip()
        if cont == "N" or cont == "S":
            break
        else:
            print("Entrada inválida.")
            cont = " "
# Processamento de dados:
media = media / cto
# Saída de dados:
print(f"A média dos valores é: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
# Fim.