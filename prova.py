'''
Exercício Python 089: Crie um programa que leia nome e duas notas de
vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
'''
lista = list()
while True:
    nome = str(input('Nome: '))
    nota1= float(input('Nota1: '))
    nota2= float(input('Nota2: '))
    media = (nota1 + nota2) /2
    lista.append([nome,[nota1,nota2],media])
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*30)
for i,v in enumerate(lista):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    elif opc <= len(lista):
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('VOLTE SEMPRE')
