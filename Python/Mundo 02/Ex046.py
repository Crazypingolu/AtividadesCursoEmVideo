'''
 - Programa: Faça um programa que mostre na tela uma contagem regressiva 
 - para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
from time import sleep
import emoji
for ano_novo in range (10, -1, -1):
    print(ano_novo)
    sleep(1)
print(emoji.emojize('🎉'))
