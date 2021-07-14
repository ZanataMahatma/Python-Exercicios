'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. '''

#correção
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
#programa principal
escreva('Gustavo Guanabara')
escreva('Cuso de Pyton no Youtube')
escreva('CeV')






#minha resposta
'''def escreva(msg):
    print('=' * len(msg))
    print(msg)
    print('=' * len(msg))

escreva('Gustavo Guanabara')
escreva('Curso de Pyton no Youtube')
escreva('CeV')
'''