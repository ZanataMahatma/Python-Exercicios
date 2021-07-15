'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
#correção
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['idade'] + (dados['contratação'] + 35) - datetime.now().year)
print('-='* 30)
for k,v in dados.items():
    print(f'  - {k} tem o valor {v}')

#minha resposta
'''from datetime import date
ctps = 0
idade = 0
anoatual = date.today().year
ano = 0
ficha = dict()
while True:
    ficha['nome'] = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    if ano != 0:
        idade = anoatual - ano
        ficha['idade'] = idade
    ctps = int(input('Carteira de Trabalho: (0 não tem)'))
    if ctps == 0:
        break
    ficha['Carteira de Trabalho'] = ctps
    ficha['AnoContratação'] = int(input('Qual o ANO de contratação ?'))
    ficha['Salário'] = float(input('Sálário: R$'))
    ficha['Aposentadoria'] = idade + 35
    break
print(ficha)
for i,v in ficha.items():
    print(f'{i} tem o valor {v}')
print(f'Ctps tem o valor {ctps}')'''
