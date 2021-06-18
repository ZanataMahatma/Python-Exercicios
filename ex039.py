from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
anoatual = date.today().year
alistamento = anoatual - ano
if  alistamento < 18:
    print('Ainda é muito Joven, vc tem {} anos e falta {} anos para se alistar.'.format(alistamento,18-alistamento))

elif alistamento == 18:
    print('Você esta com {} anos Compareça ao Alistamento Militar'.format(alistamento))
elif alistamento > 18:
    print('Já passou do tempo do alistamento seu ano atual é {} vc passou {} anos'.format(alistamento,alistamento-18))


