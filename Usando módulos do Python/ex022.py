nome= str(input('Digite o Seu Nome Completo: ')).strip() # .strip() <<<<ELIMINA A QUANTIDADE DE ESPAÇOS
print('Analizando seu Nome...')
print('Seu nome Maiusculo é {}'.format(nome.upper()))
print('Seu nome Minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
div = (nome.split())
print('Seu primeiro nome é {} e ele tem {} letras'.format(div[0], len(div[0])))
