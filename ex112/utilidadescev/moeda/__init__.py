'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''


def aumentar(preço=0, taxa=0, formato=False):
    """
    ->Calcular o aynebti de um determinado preço,
    retornando o resuldado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcetagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado,com ou sem formato.
    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    ->
    :param preço: Converter os numeros de ponto pra virgula dos prints
    :param moeda: moeda colocara em real
    :return:  Retorna um print formatado.  moeda.moeda()
    """
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0,taxaa=10,taxar=5):
    print('-'* 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do preço:\t\t{dobro(preço,True)}')
    print(f'Metade do preço:\t{metade(preço,True)}')
    print(f'Com {taxar}% de aumento:\t{aumentar(preço, taxaa,True)}')
    print(f'{taxar}% de redução:\t\t{diminuir(preço,taxar,True)}')
    print('-'* 30)