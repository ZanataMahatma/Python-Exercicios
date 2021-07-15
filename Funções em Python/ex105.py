'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode
 receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
 – Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] < 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r





#programa principal
resp = notas(9,10,5.5,2.5,8.5, sit=True)
print(resp)