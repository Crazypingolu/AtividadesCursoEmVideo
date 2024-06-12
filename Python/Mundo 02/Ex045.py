'''
 - Programa: Crie um programa que faça o computador jogar Jokenpô com você.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer bibliotecas:
from time import sleep
from random import choice
# Definir variáveis:
opcoes = ["PE", 'PA', 'T']
escolha = int
computador = str
jogador = str
# Entrada de dados:
print("{:-^30}".format("Jogo de Jokenpo")) # Título
computador = choice(opcoes) # máquina escolhe
print("A máquina já escolheu sua jogada!" +
      "\nOPÇÕES: \n[1] - Pedra\n[2] - Papel\n[3] - Tesoura")
escolha = int(input("Escolha: ")) - 1
jogador = opcoes[(escolha)]
# Processamento de dados:
sleep(0.5)
print("Processando...")
if (jogador == "PA" and computador == "PE") or (jogador == "PE" and computador == "T") or (jogador == "T" and computador == "PA"): # Condição de vitória
    sleep(1.5)
    print("JOGADOR VENCEU!")
elif (jogador == "PE" and computador == "PA") or (jogador == "T" and computador == "PE") or (jogador == "PA" and computador == "T"): # Condição de derrota
    sleep(1.5)
    print("MÁQUINA VENCEU!")
else: 
    sleep(1.5)
    print("EMPATE!")
# FIM.