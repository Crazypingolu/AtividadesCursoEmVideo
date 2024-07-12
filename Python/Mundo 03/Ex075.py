'''
 - Programa: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
 - A) Quantas vezes apareceu o valor 9.
 - B) Em que posição foi digitado o primeiro valor 3.
 - C) Quais foram os números pares.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
print(' ')
val = (int(input("Digite um valor: ")),
       int(input("Digite um valor: ")),
       int(input("Digite um valor: ")),
       int(input("Digite um valor: ")))
# Processamento + saída de dados:
print(f'Quantidade de números 9: {val.count(9)}')
if 3 in val:
    print(f'posição do 1º número 3: {val.index(3) + 1}')
else:
    print('Não existe um número 3 na tupla')
print('Números pares na tupla: ', end="")
for v in val:
    if v % 2 == 0:
        print(v, end=' ')