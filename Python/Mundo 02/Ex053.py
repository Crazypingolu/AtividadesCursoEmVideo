'''
 - Programa:  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
frase = str
fraseInvertida = str = ""
# Entrada de dados:
print('')
frase = input('Digite uma frase: ').strip().upper()
# Processamento de dados:
frase = frase.split()
frase = ''.join(frase)
for cto in range(len(frase)-1, -1, -1):
    fraseInvertida += frase[cto]
# Saída de dados:
if fraseInvertida == frase:
    print(f'A frase \033[1;34m{frase}\033[m ivertida fica \033[1;31m{fraseInvertida}\033[m, portanto é um \033[1;33mPALÍNDROMO.\033[m')
else:
    print('A frase \033[1;31mNÃO\033[m é um palíndromo.')
# Fim.