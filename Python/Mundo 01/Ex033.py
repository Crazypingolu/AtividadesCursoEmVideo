'''
 - Programa: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
nums = [0,0,0]
maior = 0
menor = int
# Entrada e Processamento de dados:
for cto in range(0,3):
    # Entrada
    nums[cto] = int(input(f"Digite o valor do {cto + 1}º número: "))
    # Processamento:
    if maior == 0: # checa se maior tem valor.
        maior = nums[cto]
        menor = nums[cto]
    else: # maior tem valor
        if maior < nums[cto]:
            maior = nums[cto]
        # fim-se
        if menor > nums[cto]:
            menor = nums[cto]
        # fim-se
    # fim-se
# Saída de dados:
print(f'''
O maior valor digitado foi: [{maior:2}]
O menor valor digitado foi: [{menor:2}]
''')
# Fim