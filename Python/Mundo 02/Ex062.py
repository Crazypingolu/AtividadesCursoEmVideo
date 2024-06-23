'''
 - Programa: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 - O programa encerrará quando ele disser que quer mostrar 0 termos.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from time import sleep
# Definir variáveis:
termo1 = int
razao = int
resultado = int
ctoIni = 0
ctoFim = 10
# Entrada de dados:
print(" ")
termo1 = int(input("\nDigite o 1º termo da PA: \n"))
razao = int(input("Digite a razão da PA: \n"))
# Processamento e retroatividade de dados:
resultado = termo1
print(f"\nOs 10 primeiros termos da PA com primeiro termo {termo1} e razão de {razao} é:")
while ctoFim != 0:
    while ctoIni < ctoFim:
# Saída de dados:
        print(f'\033[1;33m{resultado}\033[m', end=" ")
        resultado += razao
        ctoIni += 1
    ctoIni = 0
    # Entrada de parâmetro:
    ctoFim = int(input('\n\nDigite quantos mais termos o programa deve mostrar ou \ndigite 0 para finalizar o programa:\n'))
    if ctoFim != 0:
        print(f"\nOs {ctoFim} próximos termos da sequência são:")
        sleep(1)
sleep(0.5)
print("Finalizando programa.")
sleep(0.5)
# Fim.