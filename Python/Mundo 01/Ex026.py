'''
 - Programa: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
 - em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variáveis:
frase = str
quantidadeA = str
primeiroA = str
ultimoA = str
# Entrada de dados:
frase = input('\nDigite uma frase: \n')
# Processamento de dados:
frase = frase.strip().upper()
quantidade = frase.count('A')
primeiroA = frase.find('A')
ultimoA = frase.rfind('A')
# Saída de dados:
print(f'''
    Quantidade de "A" na frase: {quantidade}
    Posição do 1º "A": {(primeiroA) + 1}
    Posição do ultimo "A": {(ultimoA) + 1}
    ''')
# Fim.