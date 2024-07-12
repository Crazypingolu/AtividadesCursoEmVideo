'''
 - Programa: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 - Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
lista = ("JAVA", "PYTHON", "JAVASCRIPT", "CSS", "VISUAL BASIC", "RUBY", "PHP", "SWIFT", "GO", "SQL")
vog = int
# Processamento de dados:
print(' ')
for p in lista:
    vog = 0
    for l in p:
          if l in "AEIOU":
               vog += 1
    print(f'Na palavra {p} temos {vog} vogal(is).')
# Fim.