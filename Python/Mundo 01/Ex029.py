'''
 - Programa: Escreva um programa que leia a velocidade de um carro.
 - Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
 - A multa vai custar R$7,00 por cada Km acima do limite.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
#Trazer biblioteca:
from time import sleep
# Definir variáveis:
velo = float
# Entrada de dados:
velo = float(input('digite a velocidade do carro (em KM/H): '))
# Processamento e Saída de dados:
sleep(1)
print('Analizando dados')
sleep(1)
if velo > 80:
    print('Você foi multado. ')
    print('O valor será: {:.2f} R$. '.format((velo - 80) * 7))
else:
    print('Você não foi multado. ')
    print('Parabéns, você é um bom motorista. ')
# Fim