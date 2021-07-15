'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''


from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    ano = int(input('{} Digite o ano:'.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} Maior de Idade\n {} Menor de Idade'.format(maior,menor))
