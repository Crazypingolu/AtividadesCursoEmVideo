'''
 - Programa: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
 - Caso esteja errado, peça a digitação novamente até ter um valor correto.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Denifir variáveis:
sexo = str
aux = 0
# Entrada de dados:
print('')
while aux == 0:
    sexo = input('Escolha seu sexo: [M/F] \n').upper().strip()
# Processamento de dados:
    if sexo != 'M' and sexo != 'F':
        print('Erro, digite novamente.')
    else:
        aux = 1
# Saída de dados:
print('Entrada validada.')
# Fim.