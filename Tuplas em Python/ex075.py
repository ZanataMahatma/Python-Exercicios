'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

# correção
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')))
print(núm)
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'Posição do numero 3 está {núm.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ',end=' ')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')


# minha resposta  -.- colada  -.-
'''numero = (int(input('Digite o primeiro numero: ')),
          int(input('Digite o primeiro numero: ')),
          int(input('Digite o primeiro numero: ')),
          int(input('Digite o primeiro numero: ')))
print(f'Lista de numeros:{numero}')
print(f'O 9 apareceu {numero.index(9)} VEZES')
if 3 in numero:  #se o 3 estiver dentro da tupla
    print(f'O numero 3 foi digitado {numero.count(3)} VEZES ')
else: # senão
    print('Não foi localizado nenhum numero 3 ')
print('Numeros pares digitados',end=' ')
for n in numero:
    if n % 2 == 0:
        print(n,end=' ')'''