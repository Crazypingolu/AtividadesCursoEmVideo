'''
 - Programa: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
 - Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from random import randint
from time import sleep
# Denifir variáveis:
computador = int
player = -1
count = 0
# Entrada de dados:
print("{}".format("..." * 5))
computador = randint(0, 10)
print('O computador escolheu um número de 0 a 10 ...')
sleep(1)
while player != computador:
    sleep(0.5)
    if count != 0:
        print("Errou, tente novamente.")
    count += 1
    player = int(input('Adivinhe, qual o número escolhido? \nDigite: '))
# Saída de dados:
print(f'Acertou! \nCom \033[1;33m{count}x\033[m tentativas.')
print("{}".format("..." * 5))
# Fim.