'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação
 em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7 :
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for i,v in aluno.items():
    print(f'{i} é igual a {v}')




#minha resposta
'''dic = dict()
dic ['nome'] = str(input('Nome: '))
dic ['Média'] = float(input(f'Media de {dic["nome"]}:'))
print(f'Nome é igual a {dic["nome"]}')
print(f'Média é igual a {dic["Média"]}')
if dic['Média'] => 7:
    print('Situação é Aprovado')
else:
    print('Situação é igual a Reprovado')'''

