'''
 - Programa:Desenvolva um programa que pergunte a distância de uma viagem em Km. 
 - Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
 - R$0,45 parta viagens mais longas.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
distancia = float
passagem = float
# Entrada de dados:
distancia = float(input("\nDigite a distância da viagem: "))
# Processamento de dados:
if distancia > 200:
    passagem = 0.45 * distancia # R$0.45 por Km se a viagem for maior de 200km
else:
    passagem = 0.50 * distancia # R$0.50 por Km até 200 km
# Saída de dados:
print(f"Valor da passagem: R${passagem:.2f}")
# Fim.