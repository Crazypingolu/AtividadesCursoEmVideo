'''
 - Programa: Receber um valor e
 - mostrar sua tabuada.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variávies:
num = int
# Entrada de dados:
num = int(input("\n Digite um número (int): "))
# Processamento + saída:
print(f"| {num} x 01 = {num:5} |",
      f"\n| {num} x 02 = {(num * 2):5} |",
      f"\n| {num} x 03 = {(num * 3):5} |",
      f"\n| {num} x 04 = {(num * 4):5} |",
      f"\n| {num} x 05 = {(num * 5):5} |",
      f"\n| {num} x 06 = {(num * 6):5} |",
      f"\n| {num} x 07 = {(num * 7):5} |",
      f"\n| {num} x 08 = {(num * 8):5} |",
      f"\n| {num} x 09 = {(num * 9):5} |"
      f"\n| {num} x 10 = {(num * 10):5} |")