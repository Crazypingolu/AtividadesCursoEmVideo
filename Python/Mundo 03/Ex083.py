'''
 - Programa: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 - Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
exp = str
paren = [0, 0]
# Entrada de dados:
print(' ')
exp = str(input("Digite uma expressão: \n"))
for cto in exp:
    if cto == "(":
        paren[0] += 1
    elif cto == ")":
        if paren[0] > 0:
            paren[0] -= 1
        else:
            paren[1] += 1
# Saída de dados:
if paren[0] == paren[1]:
    print("A Expressão é válida.")
else:
    print("A Expressão é inválida.")
# Fim.    