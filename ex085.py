'''Exercício Python 085: Crie um programa onde o usuário possa digitar
ete valores numéricos e cadastre-os em uma lista única que mantenha separados
 os valores pares e ímpares. No final, mostre os valores
 pares e ímpares em ordem crescente.'''

#correção
num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores inpares digitados foram {num[1]}')


#minha resposta
'''
numero=0
par = []
impa = []
listatotal = []

for p in range(1,8):
    numero = int(input(f'Digite o {p}o. valor: '))
    if numero % 2 == 0:
        par.append(numero)
    elif numero % 2 == 1:
        impa.append(numero)
listatotal.append(par)
listatotal.append(impa)
for i,v in enumerate(listatotal):
    if v == par:
        print(f'Os valores pares digitados foram {sorted(v)}')
    else:
        print(f'Os valores impares digitados foram {sorted(v)}')
#print(f'Os valores pares digitados foram {sorted(par)}')
#print(f'Os valores impares digitados foram {sorted(impa)}')
'''

