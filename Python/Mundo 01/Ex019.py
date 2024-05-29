'''
 - Programa: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
 - Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Trazer biblioteca
import random
# Definir variáveis:
aluno01 = str
aluno02 = str
aluno03 = str
aluno04 = str
alunoAleatorio = str
listaDeAlunos = [4]
# Entrada de dados:
aluno01 = input("\nDigite o 1º nome de aluno: ")
aluno02 = input("Digite o 2º nome de aluno: ")
aluno03 = input("Digite o 3º nome de aluno: ")
aluno04 = input("Digite o 4º nome de aluno: ")
# Processamento de dados:
listaDeAlunos = [aluno01,aluno02,aluno03,aluno04]
alunoAleatorio = random.choice(listaDeAlunos)
# Saída de dados:
print(f"O aluno sorteado foi: {alunoAleatorio}")
