'''
 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e 
 - a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
 - sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
# Definir variáveis:
dias = int
km = int
conta = float
# Entrada de dados:
dias = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos quilômetros o carro percorreu: '))
# processamento de dados:
conta = (60 * dias) + (0.15 * km)
# Saída de dados:
print('O valor total a ser pago será de {}R$'.format(conta))
