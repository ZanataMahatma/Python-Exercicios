'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
ano = int(input('Digite o SEU ANO de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
 print('MIRIM sua idade atual é {} anos'.format(idade))
elif idade <=14:
    print('INFANTIL sua idade atual é {} anos'.format(idade))
elif idade <= 19:
    print('JUNIOR sua idade atual é {} anos'.format(idade))
elif idade <= 25:
    print('Sênior sua idade atual é {} anos'.format(idade))
else:
    print('MASTER sua idade atual é {} anos'.format(idade))



    '''elif 14 <= idade > 9: # forma diferente de cria uma condição
    print('INFANTIL sua idade atual é {} anos'.format(idade))
elif idade > 14 and idade <= 19:
    print('JUNIOR sua idade atual é {} anos'.format(idade))
elif idade > 19 and idade <= 20:
    print('Sênior sua idade atual é {} anos'.format(idade))
elif idade > 20:
    print('MASTER sua idade atual é {} anos'.format(idade))
'''
