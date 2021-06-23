from random import randint
r = 1
j = 0
countJ = 0
while r != j:
    j = int(input('Tente adivinhar !! de 1 a 10 :'))
    r = randint(1, 10)
    countJ = countJ + 1
    if r == j:
        print('\033[43mVocê ACERTOU\033[m')
        print('Computador escolheu: \033[33m{}\033[m'.format(r))
    else:
        print('Tente novamente')
        print('Computador escolheu \033[33m{}\033[m'.format(r))
print('Foram necessario {} JOGADAS PARA VC GANHAR'.format(countJ))
