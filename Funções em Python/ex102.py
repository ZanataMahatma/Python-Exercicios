'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba
dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo
de cálculo do fatorial.'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n:O numero a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f

#programa principal
print(fatorial(5, show=True))
#help(fatorial)

# minha resposta
'''def fatorial(num=1,show=False):
    """
    :param num: O numero a ser calculado.
    :param show: (Opcional) Mostra a ser calculado.
    :return: O valor do Fatorial de um número n.
    """
    fatorial = 1
    if show == True:
        for contador in range(num,0,-1):
            fatorial = fatorial * contador
            print(f'{contador}', end='')
            print(' x ' if contador > 1 else ' = ', end='')
        print(fatorial)
    if show == False:
        for contador in range(num,0,-1):
            fatorial = fatorial * contador
        print(fatorial)




#programa
num = int(input('Digite um numero: '))
fatorial(num)'''