'''Exercício Python 082: Crie um programa que vai ler vários números
 e colocar em uma lista. Depois disso, crie duas listas extras que
 vão conter apenas os valores pares e os valores ímpares digitados,
  respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
#correção
num = list()
pares = list()
inpares = list()

while True:
    num.append(int(input('Digite um número:')))
    resp = str(input('Deseja Coninuar? [S/N]'))
    if resp in 'Nn':
        break
for i,v in enumerate(num):
    if v % 2 == 0 :
        pares.append(v)
    elif v % 2 == 1:
        inpares.append(v)
print(f'A list completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares {inpares}')


# minha resposta.
'''lista = list()
par = list()
impa = list()
while True:
    num = int(input('Digite o Valor: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impa.append(num)
    repete = str(input('Deseja Continuar [S/N]: '))
    if repete in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impa}')'''