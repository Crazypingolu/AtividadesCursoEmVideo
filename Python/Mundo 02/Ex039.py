'''
 - Programa: Faça um programa que leia o ano de nascimento de um jovem e informe, 
 - de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
 - se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
 - Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer biblioteca:
from datetime import date
# Definir variáveis:
dataAtual = date.today().year
dataNascimento = int
idade = int
# Entrada de dados:
print("")
dataNascimento = int(input("Digite sua DATA DE NASCIMENTO: \n"))
# Processamento de dados:
idade = dataAtual - dataNascimento
# Saída de dados:
if idade < 18:
    print(f"faltam {(18 - idade)} ano(s) para fazer o alistamento.")
elif idade == 18:
    print("18 anos! se aliste ainda neste ano!")
else:
    print(f"você está atrasado {idade - 18} ano(s).")
# FIM.
