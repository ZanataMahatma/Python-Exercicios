'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

#correção
tupla = ('Bragantino','Athletico - PR','Palmeiras','Fortaleza',
         'Santos,Juventude','Bahia','Atlético - GO','Atlético - MG',
         'Corinthians','Fluminense','Flamengo,Ceará','Internacional',
         'Sport','América - MG','São Paulo','Cuiabá','Chapecoense','Grêmio')
print('=-' *15)
print(f'Os 5 primeiros são:{tupla[:6]}')
print('=-' *15)
print(f'Os 4 últimos são:{tupla[-4:]}')
print('=-' *15)
print(f'Times em ordem alfabética:{sorted(tupla)}')
print('=-' *15)
print(f'O Chapecoense está na {tupla.index("Chapecoense")+1}')
print('=-' *30)

#minha resposta

tupla = ('Bragantino','Athletico - PR','Palmeiras','Fortaleza','Santos,Juventude','Bahia','Atlético - GO'
         ,'Atlético - MG','Corinthians','Fluminense','Flamengo,Ceará','Internacional','Sport','América - MG',
         'São Paulo','Cuiabá','Chapecoense','Grêmio')
print(f'Os 5 primeiros são:{tupla[:6]}')
print(f'Os 4 últimos são:{tupla[14:18]}')
print(f'Times em ordem alfabética:{sorted(tupla)}')
print(f'Time {tupla[16]} está na posição 16')

print('='*20)
for count,times in enumerate(tupla):
    print(count,times)