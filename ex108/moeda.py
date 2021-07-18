'''
Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda() que consiga mostrar os
números como um valor monetário formatado.
'''
def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    """
    ->
    :param preço: Converter os numeros de ponto pra virgula dos prints
    :param moeda: moeda colocara em real
    :return:  Retorna um print formatado.  moeda.moeda()
    """
    return f'{moeda}{preço:>8.2f}'.replace('.',',')
