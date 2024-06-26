'''
 - Programa: Crie um programa que leia números inteiros pelo teclado. 
 - O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
 - No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Denifir variáveis:
num = int
soma = 0 
cto = 0
# Entrada de dados:
print(' ')
while True:
    num = int(input("Digite um número (999 para sair): "))
# Processamento de dados:
    if num == 999:
        break
    cto += 1
    soma += num
# Saída de dados:
print(
f'''Soma dos números: {soma}
Quantidade de números: {cto}''')
# Fim.