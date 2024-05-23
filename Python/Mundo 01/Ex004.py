'''
 - Programa: coletar uma string e verificar se:
 - é somente espaços;
 - é somente números;
 - é somente letras;
 - é totalmente maiúscula;
 - é totalmente minúscula;
 - é um alfa-numérico (letras e números);
 - se a inicial é maiuscula;
 - Programador: LucasP, Crazypingolu
 - versão: 1.0
'''
# Definir variáveis:
entrada = str
# Entrada de dados:
entrada = input("Digite: ")
# Processamento + saída:
print(f"É formada somente por espaços:    [{entrada.isspace()}]" ,
      f"\nÉ formado somento por números:    [{entrada.isnumeric()}]",
      f"\nÉ formado somene por letras:      [{entrada.isalpha()}]" ,
      f"\nEstá totalmente em maiusculo:     [{entrada.isupper()}]" ,
      f"\nEstá totalmente em minusculo:     [{entrada.islower()}]" ,
      f"\nÉ um alfa-numérico:               [{entrada.isalnum()}]" ,
      f"\nSó a letra inicial é maiuscula:   [{entrada.istitle()}]" ,
      "\n"
      )
