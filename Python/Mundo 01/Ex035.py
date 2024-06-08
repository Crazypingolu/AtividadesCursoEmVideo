'''
 - Programa: Desenvolva um programa que leia o comprimento de três retas e 
 - diga ao usuário se elas podem ou não formar um triângulo.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
ladoA = float
ladoB = float
ladoC = float
formaTriangulo = bool
# Entrada de dados:
print("")
ladoA = float(input("Digite o 1º lado: "))
ladoB = float(input("Digite o 2º lado: "))
ladoC = float(input("Digite o 3º lado: "))
# Processamento de dados:
if (ladoA + ladoB) > ladoC and (ladoA + ladoC) > ladoB and (ladoB + ladoC) > ladoA:
    formaTriangulo = True
else:
    formaTriangulo = False
# Saída de dados:
print(f"Forma triângulo: [{formaTriangulo}]")
# Fim.