'''
 - Programa: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
 - A) qual é o total gasto na compra.
 - B) quantos produtos custam mais de R$1000.
 - C) qual é o nome do produto mais barato.  
 - Programador: LucasP, Crazypingolu
 - versão: 2.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
total = 0.0
prodCaro = 0
nomeBar = str
precoBar = float
nomeEnt = str
precoEnt = float
flag = int
# Entrada de dados:
print(' ')
while True:
    nomeEnt = input("Digite o nome do produto: \n")
    precoEnt = float(input("Digite seu preço: \n"))
    if total == 0:
        nomeBar = nomeEnt
        precoBar = precoEnt
    else:
        if precoEnt < precoBar:
            nomeBar = nomeEnt
            precoBar = precoEnt
    total += precoEnt
    if precoEnt > 1000:
        prodCaro += 1
    while True:
        flag = int(input("Continuar? \n[1] - sim \n[2] - não \n"))
        if flag == 1 or flag == 2:
            break
        else:
            print('Opção inválida.')
    if flag == 2:
        break
# Saída de dados:
print(f"Total: {total:.2f}")
print(f"Produto mais barato: {nomeBar}")
print(f"Produtos acima de 1000: {prodCaro}")
# Fim.