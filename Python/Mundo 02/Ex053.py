from time import sleep
print('')
print('\033[1;33m{:-^40}\033[m'.format(' Exercício 053 '))
sleep(0.5)
print('')

pa = input('Digite uma frase: ').strip().upper()
pas = pa.split()
paj = ''.join(pas)
inver = ''
for c in range(len(paj)-1, -1, -1):
    inver += paj[c]
if inver == paj:
    print(f'A frase \033[1;34m{paj}\033[m ivertida fica \033[1;31m{inver}\033[m, portanto é um \033[1;33mPALÍNDROMO.\033[m')
else:
    print('A frase \033[1;31mNÃO\033[m é um palíndromo.')
