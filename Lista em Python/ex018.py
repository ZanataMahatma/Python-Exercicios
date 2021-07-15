import math
n1 = float(input('Digite um angulo: '))
cosseno = math.cos(math.radians(n1))
tangente = math.tan(math.radians(n1))
seno = math.sin(math.radians(n1))
print('{} \n O valor do seno é {:.2f} \nValor do cosseno {:.2f}. \nTangente {:.2f} \n {}.'.format((20*'='),seno,cosseno,tangente,(20*'=')))