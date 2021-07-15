'''Exercício Python 081: Crie um programa que vai ler vários números e
colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
#correção
valore=[]
while True:
    valore.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar? [S/M] '))
    if resp in 'Nn':
        break
print('-='* 30)
print(f'Você digitou {len(valore)} elementos.')
valore.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valore}')
if 5 in valore:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

#minha solução
'''
list_numeros = list()
cont = 0
continuar =''
num5 = False
while True:
    numero = int(input('Digite o numero:'))
    list_numeros.append(numero)
    cont = cont + 1
    if numero == 5:
        num5 = True
    continuar = str(input('Você Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'Você digitou {cont} elementos.')
list_numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {list_numeros} ')
if num5 == True:
    print('O valor 5 faz parte da lista!')
else:
    print('O numero 5 \033[35mNÃO\033[m foi localizado')


'''