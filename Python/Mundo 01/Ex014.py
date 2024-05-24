'''
 - Programa: Escreva um programa que converta uma temperatura 
 - digitando em graus Celsius e converta para graus Fahrenheit.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variávies
celsius = float
fahren = float
# entrada de dados:
celsius = float(input("Digite a temperatura em °C: "))
# Processamento de dados: 
fahren = (celsius * 9 / 5) + 32
# Saída de dados:
print(f'A temperatura {celsius}°C em fahrenheit é {fahren:.2f}°F')