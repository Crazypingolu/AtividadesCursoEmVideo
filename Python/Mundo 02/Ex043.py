'''
 - Programa: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
 - calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
 - IMC abaixo de 18,5: Abaixo do Peso
 - Entre 18,5 e 25: Peso Ideal
 - 25 até 30: Sobrepeso
 - 30 até 40: Obesidade
 - Acima de 40: Obesidade Mórbida
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Definir variáveis:
peso = float
altura = float
imc = float
# Entrada de dados:
print('')
peso = float(input("Digite seu peso: \n"))
altura = float(input("Digite sua altura: \n"))
# processamento de dados:
imc = peso / (altura * altura)
# Saída de dados:
if imc < 18.5:
    print("Abaixo do peso.")
elif imc <= 25:
    print("Peso ideal.")
elif imc <= 30:
    print("Sobrepeso.")
elif imc <= 40:
    print("Obesidade.")
else:
    print("Obesidade mórbida.")
# Fim.
