'''
 - Programa: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
 - No final do programa, mostre: a média de idade do grupo, 
 - qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Denifir variáveis:
nomeEntrada = str
idadeEntrada = int
sexoEntrada = int
mediaIdade = 0
nomeHMaisVelho = ""
idadeHmaisVelho = 0
quantMMenosDe20 = 0
# Entrada de dados:
for cto in range(1, 5, 1):
    nomeEntrada = input(f"Digite o NOME da {cto}º pessoa: \n")
    idadeEntrada = int(input(f"Digite o IDADE da {cto}º pessoa: \n"))
    sexoEntrada = int(input(f"Digite o SEXO (biológico) da {cto}º pessoa:" +
                            "\n[1] - Masculino. \n[2] - Feminino. \n"))
# Processamento de dados (dentro do for):
    # Soma a idade pro cálculo da média fora do loop.
    mediaIdade += idadeEntrada
    # Verifica se é um homem e se a idade dele for maior que a do homem mais velho registrado ou se não tem registro de mais velho.
    if sexoEntrada == 1 and nomeHMaisVelho == "" or sexoEntrada == 1 and idadeHmaisVelho < idadeEntrada:
        nomeHMaisVelho = nomeEntrada
        idadeHmaisVelho = idadeEntrada
    # Verifica se é uma mulher e se a idade dela é menor que 20. 
    elif sexoEntrada == 2 and idadeEntrada < 20:
        quantMMenosDe20 += 1
# Calcular a média:
mediaIdade = mediaIdade / 4
# Saída de dados:
print(f"Nome do homem mais velho: {nomeHMaisVelho}")
print(f"Quantidade de mulheres abaixo de 20 anos: {quantMMenosDe20}")
print(f"Média das idades: {mediaIdade}")
# Fim.