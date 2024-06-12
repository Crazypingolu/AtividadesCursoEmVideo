'''
 - Programa: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
 - à vista dinheiro/cheque: 10% de desconto
 - à vista no cartão: 5% de desconto
 - em até 2x no cartão: preço formal
 - 3x ou mais no cartão: 20% de juros
 - Programador: LucasP, Crazypingolu
 - versão: 2.0
'''
# Trazer bibliotecas:
from time import sleep
# Definir variáveis:
preco = float
parcela = -1
menu = 0
# Entrada de dados:
print("")
preco = float(input("Digite o preço do produto: \n"))
while (menu != 9):
    sleep(0.5)
    menu = int(input("\nEscolha o método de pagamento: \n" +
                     "[1] - à vista dinheiro/cheque (10% de desconto)\n" +
                     "[2] - à vista cartão (5% de desconto)\n" +
                     "[3] - em 2x no cartão \n" +
                     "[4] - 3x ou mais no cartão (20% de juros)\n" +
                     "[9] - Sair.\n"))
# Saída de dados:
    match menu:
        case 1:
            sleep(0.5)
            print(f"Valor à pagar {(preco * 0.9):.2f}")
        case 2:
            sleep(0.5)
            print(f"Valor à pagar {(preco * 0.95):.2f}")
        case 3:
            sleep(0.5)
            print(f"Valor à pagar por mês: {(preco / 2):.2f}" +
                  f"\nValor total: {preco}")
        case 4:
            sleep(0.5)
            while parcela == -1:
                sleep(0.5)
                parcela = int(input("Digite a quantidade de parcelas (maior que 2 parcelas)\nDigite [0] para cancelar: \n"))
                if parcela == 0:
                    sleep(0.5)
                    print("..."*9)
                elif parcela < 3:
                    sleep(0.5)
                    print("Opção inválida.")
                    parcela = -1
                else:
                    sleep(0.5)
                    print(f"Valor à pagar por mês: {((preco / parcela) * 1.2):.2f}" +
                          f"\nValor total: {(preco * 1.2):.2f}")
                # Fim - se
            # Fim - While
            parcela = -1
        case 9:
            sleep(0.5)
            print("..." * 9)
        case _:
            sleep(0.5)
            print("Opção inválida.")
        # Fim - match
    # Fim - While
# Fim.