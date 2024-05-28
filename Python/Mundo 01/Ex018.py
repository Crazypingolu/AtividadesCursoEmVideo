import math
an = float(input('Digite um ângulo: '))
an1 = math.radians(an)
print('o cosseno do ângulo de {}° é {:.2f} \no seno do ângulo {}° é {:.2f} \na tangente do ângulo {}° é {:.2f}'.format(an, math.cos(an1), an, math.sin(an1), an, math.tan(an1)))
