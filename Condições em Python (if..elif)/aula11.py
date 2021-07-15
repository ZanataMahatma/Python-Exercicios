#print('\033[7;33;44mOla Mundo\033[m')     comando para coloca as cores

nome = 'Zanata'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
          'pretoebranco':'\033[7;40m'}
print('Ola !!!  Prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))