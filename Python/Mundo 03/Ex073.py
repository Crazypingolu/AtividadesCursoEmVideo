'''
 - Programa: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
 - a) Os 5 primeiros times.
 - b) Os últimos 4 colocados.
 - c) Times em ordem alfabética. 
 - d) Em que posição está o time da Chapecoense.
 - Programador: LucasP, Crazypingolu
 - versão: 1.0.0
'''
# Trazer bibliotecas:
# Definir variáveis:
times = ('flamengo','botafogo','palmeiras','são paulo','bahia','athletico-pr','cruzeiro','fortaleza','red bull bragantino','internacional',
         'juventude','atlético-mg','vasco','criciúma','vitória','cuiabá','corinthians','grêmio','atlético-go', 'fluminense') # 10/07/2024
# Processamento + saída de dados:
print(' ')
# a):
print(f'Os primeiros 5 times são: {times[:5]}')
# b):
print(f'Os últimos 4 colocados: {times[-4:]}')
# c):
print(f'Os times em ordem alfabética: {sorted(times)}')
# d):
if 'chapecoense' in times:
    print(f'Posição do chapecoense: {times.index("chapecoense") + 1}')
else:
    print("Chapecoense não está nos 20 primeiros colocados.")