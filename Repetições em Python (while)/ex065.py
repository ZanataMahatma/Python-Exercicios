
'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''



repete = 'S'
count = soma = media = maior = menor = 0
while repete =='S':
    num = int(input('Digite um número: '))
    count = count + 1
    soma = soma + num
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    repete = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
media = soma / count

print('Você digitou {} números e a média foi {}'.format(count,media))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))