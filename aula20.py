def titulo(txt):
    print('-=' * 20)
    print(txt)
    print('-=' * 20)

titulo('            CURSO EM VÍDEO ')
#titulo(' APRENDA PYTHON ')
#titulo(' GUSTAVO GUANABARA ')


def soma(a, b):
    print(f'O valor de {a} + {b}', end=' ')
    s = a + b
    print(f'Resultado {s}')

#programa principal
soma(4, 5)
soma(a=8, b=9) # pode troca a ORDEM
soma(2, 1)


#empacotamento...
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores de {num}e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

'''   for v in num:
       print(f'{v} ', end='')
   print('FIM')'''


def soma(* valores):
    s = 0
    for numero in valores:
        s = s + numero
        print(f'Soma dos {valores} temos {s}')

soma(2, 5, 6)
soma(6, 47, 8)



def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos]*= 2
        pos = pos + 1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)


