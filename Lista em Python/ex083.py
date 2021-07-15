'''Exercício Python 083: Crie um programa onde o usuário digite uma
expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os
parênteses abertos e fechados na ordem correta.'''

expr = str(input('Digite a expressão'))
pilha= []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expreção está Válida!')
else:
    print('Sua expreção está errada!')
