'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro')

for p in palavras: # para cada posição  das palavras
    print(f'\nNa palavra {p.upper()} temos - ',end='') #imprima posição.
    for letra in p:#
        if letra.lower() in 'aeiou':#para cada letra da posição, se a letra conter  'aeiou'
            print(letra,end=' ')#imprima letra.




'''
palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro')
for posição in palavras:
    print(f'\nVogais de {posição.upper()} é: ',end='')
    for letra in posição:
        if letra in 'aeiou':
            print(letra,end=' ')
'''





























