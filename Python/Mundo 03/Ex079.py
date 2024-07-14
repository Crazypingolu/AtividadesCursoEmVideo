'''
 - Programa: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 - Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
nums = list()
num = int
fim = str
# Entrada e validação de dados:
print(' ')
while True:
    num = int(input("Digite um número para ser adicionado na lista: \n"))
    if num in nums:
        print("\nNúmero já está na lista, ", end='')
    else:
        nums.append(num)
    while True:
        fim = input("continuar?\nDigite [n]/[s]: \n")
        if fim not in "sSnN":
            print('\nOpção inválida, ', end="")
        else:
            break
    if fim in "Nn":
        break
# Processamento de dados:
nums.sort()
# Saída de dados:
print("Os números digitados em ordem crescente é: \n", *nums)
# Fim.