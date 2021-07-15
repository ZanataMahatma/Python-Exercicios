'''Exercício Python 076: Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

#TREINANDO ............
prod = ('arroz',25,
        'feijão',99.40,
        'macarrão',20,
        'óleo',3,
        'azeite',2.50,
        'tempero pronto',1,
        'maionese',10,
        'extrato de tomate',15,
        'enlatados',25.00,
        'farinhas',18,
        'café',21,
        'chá',1.50,
        'leite',5)
print('-'*40)
print(f'{"LISTA DE PREÇO":^40}')
print('-'*40)
for pos in range(0,len(prod)):
    if pos % 2 ==0:
        print(f'{prod[pos]:.<30}',end='')
    else:
        print(f'R${prod[pos]:>7.2f}')
print('-'*40)

#correção
'''listagem = ('Lápis',1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  #:^40     40 espaços  ^ CENTRALIZADO
print('-' * 40)
# para cada posição vai seguir  listagem o tamanho da listagem
for pos in range(0,len(listagem)):
    if pos % 2 == 0: # se posição tiver o resto igual a 0
        print(f'{listagem[pos]:.<30}',end='')   # coluna par   :. Pontos  :< Alinhado a Esquerda   :30 é a quantidade de caracteres
    else:
        print(f'R${listagem[pos]:>7.2f}') # coluna impa :>7.2f   7 caracteres > alinhados  a direita   .2f é para mostra com 2 casas decimais.
print('-' * 40)
'''

