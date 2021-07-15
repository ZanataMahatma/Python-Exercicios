'''
Exercício Python 089: Crie um programa que leia nome e duas notas de
vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Notas1: '))
    nota2 = float(input('Notas2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])  # Lista composta    nome = 0   [ nota1,nota2] = 1 , media = 2
    resp = str(input('Deseja continuar ? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') # Cabeçalho de um Boletim
print('-' * 26)
for i,a in enumerate(ficha):    # Varrendo a Ficha para printa as informações dentro do boletin
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # i =  a = o INDICE   a[0] = NOME DAS NOTAS    a[2] =  MEDIA
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<VOLTE SEMPRE>>>')