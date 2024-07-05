'''
 - Programa:  Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 - Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
ent = int
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseies", "dezesete", "dezoito", "dezenove", "vinte")
# Entrada de dados:
print(' ')
while True:
    ent = int(input("Digite um número entre 0 e 20: \n"))
    if ent < 21 and ent > -1:
        break
    else:
        print('opção inválida, ', end="")
# Saída de dados:
print(f'O número digitado por extenso é: {numeros[ent]}')
# Fim.