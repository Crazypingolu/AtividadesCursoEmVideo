'''
 - Programa: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
 - o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
 - A) quantas pessoas tem mais de 18 anos.
 - B) quantos homens foram cadastrados.
 - C) quantas mulheres tem menos de 20 anos. 
 - Programador: LucasP, Crazypingolu
 - versão: 2.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
sexoEnt = int
idadeEnt = int
qntMul = 0
qntHom = 0
qntMIdade = 0
flag = int
# Entrada de dados:
print(' ')
while True:
    idadeEnt = int(input("Digite a idade: \n"))
    while True:
        sexoEnt = int(input("[1] - Masculino \n[2] - Feminino \n"))
        if sexoEnt == 1 or sexoEnt == 2:
            break
        else:
            print('Opção inválida.')
# Processamento de dados:
    if idadeEnt > 18:
        qntMIdade += 1
    if sexoEnt == 2 and idadeEnt < 20:
        qntMul += 1
    elif sexoEnt == 1:
        qntHom += 1
    while True:
        flag = int(input("Continuar? \n[1] - sim \n[2] - não \n"))
        if flag == 1 or flag == 2:
            break
        else:
            print('Opção inválida.')
    if flag == 2:
        break
# Saída de dados:
print(f"{qntMIdade} maiores de idade.")
print(f'{qntHom} homens foram cadastrados.')
print(f'{qntMul} mulheres cadastradas abaixo de 20 anos.\n')
# Fim.