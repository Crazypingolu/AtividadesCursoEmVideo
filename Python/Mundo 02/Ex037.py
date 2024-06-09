'''
 - Programa: Escreva um programa em Python que leia um número inteiro qualquer e 
 - peça para o usuário escolher qual será a base de conversão: 
 - 1 para binário
 - 2 para octal 
 - 3 para hexadecimal.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
loopEntrada = int
numInt = int
# Entrada de dados:
loopEntrada = 0
numInt = int(input("Digite um número inteiro: "))
while loopEntrada != 9:
    loopEntrada = int(input("ESCOLHA: " +
                            "\n[1] - Converter em binário." +
                            "\n[2] - Converter em Octal." +
                            "\n[3] - Converter em Hexa." +
                            "\n[9] - FIM.\n"))
    # Processamento + Saída:
    match loopEntrada:
        # Saída de dados:
        case 1:
            print(f"O número {numInt} convertido em binário é: {bin(numInt)[2:]}")
        case 2:
            print(f"O número {numInt} convertido em Octal é: {oct(numInt)[2:]}")
        case 3:
            print(f"O número {numInt} convertido em Hexadecimal é: {hex(numInt)[2:]}")
# FIM