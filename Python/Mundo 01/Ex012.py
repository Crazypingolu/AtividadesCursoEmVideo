'''
 - Programa: Faça um algoritmo que leia o preço de um produto e 
 - mostre seu novo preço, com 5% de desconto.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variávies:
produtoOriginal = float
produtoReajuste = float
# Entrada de dados:
produtoOriginal = float(input("Digite o valor do produto: "))
# Processamento de dados:
produtoReajuste = produtoOriginal * 0.95
# Saída de dados:
print(f"O produto com 5% de desconto é: {produtoReajuste}")
