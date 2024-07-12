'''
 - Programa: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 - No final, mostre uma listagem de preços, organizando os dados em forma tabular.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
precos = ("Lapiseira", 4.99,
          "Borracha", 0.99,
          "Caderno", 11.99,
          "Lápis", 1.49,
          "Pasta", 19.99,
          "Agenda", 8.50,
          "Régua", 7.99,
          "Caneta", 2)
# Saída de dados:
print(' ')
print(f'{"-" * 40}')
print(f'{"Loja Digital":^40}')
print(f'{"-" * 40}')
for p in range(0, len(precos)):
    if p % 2 == 0:
        print(f'{precos[p]:.<30}', end='')
    else:
        print(f'R${precos[p]:>8}')
print(f'{"-" * 40}')
# Fim.