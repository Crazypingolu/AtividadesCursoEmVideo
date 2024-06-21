'''
 - Programa: Crie um programa que leia dois valores e mostre um menu na tela:
 - [ 1 ] somar
 - [ 2 ] multiplicar
 - [ 3 ] maior
 - [ 4 ] novos números
 - [ 5 ] sair do programa
 - Seu programa deverá realizar a operação solicitada em cada caso.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from time import sleep
# Definir variáveis:
num1 = int
num2 = int
resul = int
menu = 0
# Loop - Entrada de dados:
print('')
num1 = int(input('Digite o 1º número: \n'))
num2 = int(input('Digite o 2º número: \n'))
while menu != 5:
    sleep(1)
    menu = int(input("\nMenu de Opções: " +
                     "\n[ 1 ] - Somar os números." +
                     "\n[ 2 ] - Multiplicar os números." +
                     "\n[ 3 ] - Maior número." +
                     "\n[ 4 ] - Digitar outros números." +
                     "\n[ 5 ] - Finalizar programa." + 
                     "\nEscolha: \n"))
# Processamento de dados e saída:
    match menu:
        case 1:
            resul = num1 + num2
            # saída da soma.
            print(f'A soma de \033[32m{num1}\033[m e \033[32m{num2}\033[m é: \033[1;33m{resul}\033[m')
        case 2:
            resul = num1 * num2
            # saída da multiplicação.
            print(f'A multiplicação de \033[32m{num1}\033[m por \033[32m{num2}\033[m é: \033[1;33m{resul}\033[m')
        case 3:
            if num1 != num2:
                if num1 > num2:
                    resul = num1
                elif num2 > num1:
                    resul = num2
                # saída do maior número, se existir.
                print(f'O maior entre \033[32m{num1}\033[m e \033[32m{num2}\033[m é: \033[1;33m{resul}\033[m')
            else:
                # saída da igualdade.
                print('\033[1;32mOs números são iguais.\033[m')    
        case 4:
            num1 = int(input('Digite o 1º número: \n'))
            num2 = int(input('Digite o 2º número: \n'))
        case 5:
            # Fim do programa.
            print("Finalizando programa...")
        case _:
            # validação da opção
            print("\033[1;31mOpção inválida\033[m, digite novamente.")
# Fim.