'''
 - Programa: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
 - pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
 - OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
saque = int
total = int
not50 = 0
not20 = 0
not10 = 0 
not1 = 0
# Entrada de dados:
print(' ')
saque = int(input('Digite o valor do saque: '))
total = saque
# Processamento e saída de dados:
while True:
    if total // 50 > 0:
        not50 = total // 50
        print(f"{not50}x notas de R$50.00 ")
        total = total - (not50*50)
    elif total // 20 > 0:
        not20 = total // 20
        print(f"{not20}x notas de R$20.00 ")
        total = total - (not20*20)
    elif total // 10 > 0:
        not10 = total // 10
        print(f"{not10}x notas de R$10.00 ")
        total = total - (not10*10)
    elif total // 1 > 0:
        not1 = total // 1
        print(f"{not1}x notas de R$1.00 ")
        total = total - not1
    elif total == 0:
        break
print("Fim.")
# Fim