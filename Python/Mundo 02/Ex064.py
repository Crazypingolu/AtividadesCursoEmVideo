'''
 - Programa:  Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, 
 - que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from time import sleep
# Definir variáveis:
num = 0
soma = 0
cont = 0
# Entrada de dados:
print(' ')
while num != 999:
    print("Digite [999] para terminar o programa:")
    sleep(0.5)
    num = int(input("Digite um valor: "))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
# Saída de dados:
sleep(1)
print(f'\nSoma de todos os valores: {soma}')
sleep(0.5)
print(f'\nQuantidade de números somados: {cont}')
# Fim.