'''Exercício Python 079: Crie um programa onde o usuário possa digitar
 vários valores numéricos e cadastre-os em uma lista.
  Caso o número já exista lá dentro, ele não será adicionado.
  No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

# criando uma lista sem deixa entrar valores duplicados
lista = []
while True:
    v = int(input('Digite um valor: ')) # foi criando uma variavel
    if v not in lista:  # se 'V' não estiver nos numeros
        lista.append(v)  # adiciona na lista.
        print('Valor Adicionado com Sucesso.')
    else:
        print('Numero duplicado')
    r = str(input('Quer Continuar [S/N] '))
    if r in 'Nn':
        break
print(f'Você Digitou os Valores {sorted(lista)}')


'''
numero = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in numero:           # se 'n' não estiver nos numeros
        numero.append(n)           # adiciona os numeros
        print('Valor adicionado com sucesso...')
    else:
        print('Valor Duplicado! Não vou adicionar...')
    r = str(input('Quer Coninuar? [S/N] '))
    if r in 'Nn':  # se r for 'N' -usuario digitar N
        break        # derruba o loop
print('-=' * 30)
print(f'Você Digitou os valores {numero}')'''
