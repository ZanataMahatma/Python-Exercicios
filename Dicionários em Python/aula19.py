pessoas = {'nome': 'Gustavo', 'Sexo': 'M','idade': 22}
'''print(pessoas[0]) Não funciona para dicionarios'''
#del pessoas['sexo']  para apagar
pessoas['nome'] = 'Leandro' #substitindo o nome gustavo por Leandro.
pessoas['peso'] = 95.5 #Comando para adicionar um elemento no dicionario

print(pessoas['idade']) # primeiramente o nome do dicionario e logo seguida o nome do objeto para consulta o valor
print('-='* 30)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-='* 30)
print(pessoas.keys())
print('-='* 30)
print(pessoas.values())
print('-='* 30)
print(pessoas.items())
print('-='* 30)
for k in pessoas.keys():
    print(k)
print('-='* 30)
for k in pessoas.values():
    print(k)
print('-='* 30)
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('>>>>>>>>>>>''Criando dicionario dento de uma lista')
#Criando um Dicionario dentro de uma lista.
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'Sigla' : 'RJ'}
estado2 = {'uf':'São Paulo','Sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: ')) # Lendo para dentro do dicionario
    estado['sigla'] = str(input('Sigla do Estado: ')) # lendo para dentro do dicionario
    brasil.append(estado.copy())  # adicionando para dentro da lista
for e in brasil: # for de fora para lista.
    for v in e.values():  #for  para o dicionario
        print(v, end=' ')
    print()



