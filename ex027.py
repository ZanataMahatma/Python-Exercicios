nome= str(input('Digite seu nome Completo: ')).strip()
print('Prazer em te conhecer !')
lista = nome.split()
print(('Seu Primeiro nome é {} '.format(lista[0])))
print('Seu Ultimo nome é {}'.format(lista[len(nome)-1]))
