'''
 - Programa: Receber u valor em R$ e
 - converter em Dolar, iene e Euro.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variávies:
real = int
dolar = float
euro = float
iene = float
# Entrada de dados:
real = int(input("\n Digite o valor (em reais): "))
# Processamento de dados:
dolar = real / 5.1
euro = real / 5.59
iene = real / 0.033
# Saída de dados:
print(f"Real para Dolar: {dolar:.2f}",
      f"Real para Euro:  {euro:.2f}",
      f"Real para Iene:  {iene:.2f}")