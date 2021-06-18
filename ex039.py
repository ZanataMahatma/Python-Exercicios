'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora
 exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
 o tempo que falta ou que passou do prazo.'''


from datetime import date
nasc = int(input('Informe o seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
if idade == 18:
    print('Você esta com {} anos Compareça ao Alistamento Militar'.format(idade))
elif  idade < 18:
    saldo = 18 - idade
    print('Ainda é muito Joven, vc tem {} anos e falta {} anos para se alistar.'.format(idade,saldo))
    ano = anoatual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Já passou do tempo do alistamento seu ano atual é {} vc passou {} anos'.format(idade,saldo))
    ano = anoatual - saldo
    print('Seu alistamento foi em {}'.format(ano))

