
# import math # biblioteca de matematica  importando todas as  funcionalidade do MATH
import math
from math import sqrt   #  <<<<<<< IMPORTANDO PARCIALMENTE NO CASO DESTE EXEMPLO IMPORTANTO A RAIZ QUADRADA SQRT
num = int(input('Digite um numero: '))
raiz = math.sqrt(num) # sqrt << raiz quadrada da biblioteca
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))          #ceil arrendoda o numero para cima float
                                                                 #floor arrendoda o numero para baixo float

