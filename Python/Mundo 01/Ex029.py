from time import sleep
velo = float(input('digite a velocidade do carro (em KM/H): '))
sleep(1)
print('Analizando dados')
sleep(1)
if velo > 80:
    print('Você foi multado. ')
    print('O valor será: {:.2f} R$. '.format((velo - 80) * 7))
else:
    print('Você não foi multado. ')
    print('Parabéns, você é um bom motorista. ')
