# Trazer biblioteca
from math import sqrt
# Definir variáveis:
ca = float
cd = float
hip = float
# Entrada de dados:
ca = float(input('Valor do cateto oposto: '))
cd = float(input('Valor do cateto adjacente: '))
# Processamento de dados:
hip = sqrt((ca * ca) + (cd * cd))
#---Ou fazer math.hypot(ca, cd)---#
# Saída de dados:
print('A hipotenusa dos valores é {:.2f}'.format(hip))
