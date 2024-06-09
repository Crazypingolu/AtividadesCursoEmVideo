'''
 - Programa: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 - Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 - A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
valorCasa = float
salComprador = float
anosPagamento = float
prestacao = float
emprestimoValido = bool
# Entrada de dados:
valorCasa = float(input("Digite o valor da CASA: \n"))
salComprador = float(input("Digite o valor do SALÁRIO: \n"))
anosPagamento = float(input("Digite em quantos ANOS o valor será pago: \n"))
# Processamento de dados:
prestacao = valorCasa / (anosPagamento * 12)
if prestacao > (salComprador * 0.3):
    emprestimoValido = False
else:
    emprestimoValido = True
# Saída de dados:
if emprestimoValido == True:
    print("O empréstimo pode ser efetuado!")
else:
    print("O empréstimo está negado.")
# Fim