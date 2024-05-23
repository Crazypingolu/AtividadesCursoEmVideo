'''
 - Programa: Receber um número inteiro e mostrar
 - seu antecessor e seu sucessor.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variáveis:
num = int
# Entrada de dados:
num = int(input("\nDigite um número (inteiro): "))
# Processamento e saída de dados:
print(f"O antecessor do número {num} é {(num - 1)}",
      f"\nO sucessor do número {num} é {(num + 1)}")
