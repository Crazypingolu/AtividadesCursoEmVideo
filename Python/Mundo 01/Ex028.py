'''
 - Programa: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
 - e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
 - O programa deverá escrever na tela se o usuário venceu ou perdeu.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
#Trazer biblioteca:
from random import randint
# Definir variáveis:
numComputador = int
numUsuario = int
resultado = str
# Entrada de dados:
print("..."*5)
numComputador = randint(0,5)
print("O computador escolheu (aleatóriamente) um número entre [0] e [5].")
numUsuario = int(input('Tente acertar \nDigite um número ente 0 e 5: \n'))
# Processamento de dados:
if numUsuario == numComputador:
    resultado = "Acertou!"
else:
    resultado = "Errou, tente novamente!"
# Saída de dados:
print(resultado)
print("..."*5)
# Fim