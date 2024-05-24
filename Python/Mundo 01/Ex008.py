'''
 - Programa: Receber um valor em metros e
 - conventer em km, cm e mm.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variáveis:
metros = int
# Entrada de dados:
metros = int(input("\nDigite um valor (em metros): "))
# Processamento e saída de dados:
print(f"\nO valor em Mm é {metros * 1000}",
      f"\nO valor em Cm é {metros * 100}", 
      f"\nO valor em Km é {metros / 1000}")