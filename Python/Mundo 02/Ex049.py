'''
 - Programa: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
num = int
# Entrada de dados:
print("")
num = int(input("Digite um número, o programa irá mostrar sua tabuada: "))
# Saída + Processamento
for cto in range(1, 11, 1):
    print(f"{num} x {cto:02} = {(num*cto)}")
# Fim.