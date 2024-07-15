'''
 - Programa: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
 - A) Quantos números foram digitados.
 - B) A lista de valores, ordenada de forma decrescente.
 - C) Se o valor 5 foi digitado e está ou não na lista. 
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
listaNum = []
num = int
cto = 0
fim = str
# Entrada e validação de dados:
print(' ')
while True:
    num = int(input('Digite um número: \n'))
    listaNum.append(num)
    cto += 1
    while True:
        fim = int(input('continuar?\n[1] - Sim\n[2] - Não\nDigite: '))
        if fim == 1 or fim == 2:
            break
        else:
            print('Opção inválida, ', end='')
    if fim == 2:
        break
# Processamento de dados:
listaNum.sort(reverse=True)
# Saída de dados:
print(f'{cto} números foram digitados.')
print('Os números digitados (em ordem decrescente):\n', *listaNum)
if 5 in listaNum:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
# Fim.