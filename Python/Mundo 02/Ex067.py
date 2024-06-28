'''
 - Programa: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
 - O programa será interrompido quando o número solicitado for negativo. 
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Denifir variáveis:
num = int
cto = 0
resultado = int
# Entrada de dados:
print(' ')
while True:
    num = int(input("\nDigite um valor para o programa mostrar sua tabuada," +
                    "\nPara finalizar o programa digite um valor negativo: \n"))
# Processamento de dados:
    if num < 0:
        break
    else:
        for cto in range(1, 11, 1):
            resultado = cto * num
# Saída de dados:
            print(f"{num} x {cto} = {resultado} ", end=", ")
        print("Fim da tabuada.")
print("\nFim do programa.")
# Fim.