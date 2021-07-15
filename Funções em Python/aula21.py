def somar(a=0,b=0,c=0):
    """

    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    Função criada para aprender
    """
    s = a + b + c
    print(f'A soma vale {s}')
somar(b=3,c=5)

#escopo de variaveis
def teste ():
    x = 8 # Vareavel Local valida somente dentro da função
    print(f'Na na função , n vale {n}')
    print(f'Na função x vale {x}')

# programa Principal
n =2 # vareavel global
print(f'No programa principal , n vale {n}')

# retornando valores de função

def somar(a=0,b=0,c=0):
    s = a +b+c
    return s # retorno para enviar para  uma variavel os resultados.


r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)
print(f'Os resultados foram {r1},{r2} e {r3}')




def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um Numero: '))
if par(num):
    print(f'é par')
else:
    print('Não é Par!')