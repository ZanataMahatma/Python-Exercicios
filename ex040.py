produto = float(input('Insira o Valor do Produto: '))
lista = int(input('Digite a forma de pagamento.\n 1 - Dinheiro\n 2 - Cheque\n 3 - Cartão\n Digite: '))
if lista != 1 and lista != 2 and lista != 3:
    print('Comando Invalido... Tente Novamente.')