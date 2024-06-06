'''
 - Programa: Faça um programa que leia o nome completo de uma pessoa, 
 - mostrando em seguida o primeiro e o último nome separadamente.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variáveis:
nome = str
nomeSplit = str
# Entrada de dados:
nome = input('\nDigite seu nome completo: \n').strip()
# Processamento de dados:
nomeSplit = nome.split()
# Saída de dados:
print(f'''
Primeiro nome:  {nomeSplit[0]}
Último nome:    {nomeSplit[(len(nomeSplit)) - 1]}
''')
# FIM