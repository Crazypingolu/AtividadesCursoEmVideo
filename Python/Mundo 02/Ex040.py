'''
 - Programa: Crie um programa que leia duas notas de um aluno e calcule sua média, 
 - mostrando uma mensagem no final, de acordo com a média atingida:
 - Média abaixo de 5.0: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
nota1 = float
nota2 = float
media = float
# Entrada de dados:
print("")
nota1 = float(input("Digite a 1º nota: \n"))
nota2 = float(input("Digite a 2º nota: \n"))
# Processamento de dados:
media = (nota1 + nota2) / 2
# Saída de dados:
if media < 5:
    print("REPROVADO.")
elif media < 6.9:
    print("RECUPERAÇÃO.")
else:
    print("Aprovado!")
# FIM.