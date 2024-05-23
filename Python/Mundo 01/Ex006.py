'''
 - Programa: Receber um número inteiro e mostrar
 - seu dobro, triplo e raiz.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Trazer elemento da biblioteca
from math import sqrt
# Definir variáveis e receber dados:
num = int(input("\nDigite um número (int): "))
# Processamento + saída:
print(f"O dobro do número {num} é {(num * 2)}", 
      f"\nO triplo do número {num} é {(num * 3)}", 
      f"\nA raiz de {num} é {(sqrt(num)):.2f}")