'''
 - Programa:  Faça um programa que leia a largura e a altura de uma parede em metros,
 - calcule a sua área e a quantidade de tinta necessária para pintá-la,
 - sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variávies:
alt = float
lar = float
area = float
tintaGasta = float
# Entrada de dados:
alt = float(input(" \nDigite a altura da parede a ser pintada: "))
lar = float(input("Digite a largura da parede a ser pintada: "))
# Processamento de dados:
area = alt * lar
tintaGasta = area / 2 # 4m² / 2 = 2m²
# Saída de dados:
print(f"Uma parede de área {area:.2f}, \ngasta {tintaGasta:.2f}L de tinta.")