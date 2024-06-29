'''
 - Programa: Faça um programa que jogue par ou ímpar com o computador. 
 - O jogo só será interrompido quando o jogador perder, 
 - mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer bibliotecas:
from random import randint
# Denifir variáveis:
comp = int
jogador = int
parOuImpar = int
vito = 0
# Entrada de dados:
print(' ')
while True:
    comp = randint(1, 10) # número aleatório
    while True: # Validação de paro ou impar
        parOuImpar = int(input("\nEscolha: \n[1] - Par \n[2] - impar\n")) 
        if parOuImpar == 2 or parOuImpar == 1:
            break
        else:
            print("Valor inválido.")
    # Entrada de um número pelo jogador:
    jogador = int(input("Digite um número: \n"))
    jogador += comp
    # Validação de vitória:
    if jogador % 2 == 0 and parOuImpar == 1 or jogador % 2 != 0 and parOuImpar == 2:
        vito += 1
        print('Você ganhou!')
    else:
        break
# Saída:
print(f"\nVitórias alcançadas: {vito}x")
# Fim.