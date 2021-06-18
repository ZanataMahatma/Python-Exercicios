from time import sleep
produto = float(input('Insira o Valor do Produto: '))
lista = int(input('Digite a forma de pagamento.\n 1 - Dinheiro\n 2 - Cheque á Vista\n 3 - Cartão\n Digite: '))
desc = (produto * 1.10) - produto
totaldesc = produto - desc
if lista != 1 and lista != 2 and lista != 3:
    print('Comando Invalido... Tente Novamente.')
elif lista == 1:
    print('Forma de pagamento escolhida foi: Dinheiro ',end=(''))
    print('\033[1;30;41mProcessando Desconto...\033[m')
    sleep(2)
    print('Valor total do Produto: R${:.2f} com 10% desconto aplicado R${:.2f}\n Valor Total a pagar: \033[1;30;43mR${:.2f}\033[m'.format(produto,desc,totaldesc))
elif lista == 2:
    print('Pagamento com Cheque á vista terá 10% desconto...\n Valor total R${:.2f}\n Valor com Desconto \033[1;30;43mR${:.2f}\033[m'.format(produto,totaldesc))
elif lista == 3:
    desc2= (produto*1.05)-produto
    totaldesc2 = produto-desc2
    lista2 = int(input('Deseja Parcela?\n Digite 1 ou 2 escolha as opções...\n 1- Cartão 1x\n 2- Cartão 2x\n 3- Cartão 3x\n Digite: '))
    print('\033[1;30;41mProcessando...\033[m')
    sleep(2)
    if lista2 !=1 and lista2 !=2 and lista2 !=3:
        print('Comando de Parcelamento INVALIDO...')
    elif lista2 == 1:
        print('Cartão x1 Escolhido.. Valor total R${:.2f} com desconto 5% aplicado R${:.2f}\n Valor Total a pagar: \033[1;30;43mR${:.2f}\033[m.'.format(produto,desc2,totaldesc2))
    elif lista2 == 2:
       print('Cartão x2 Escolhido...\n \033[1;30;43mValor total R${:.2f} x2\033[m\n Parcela 1 R${:.2f}\n Parcela 2 R${:.2f}'.format(produto,produto/2,produto/2))
    else:
        lista2 == 3
        n = 3
        i = 0.20
        juros = ((1+i)**3)-1
        juros2 = ((1+i)**3)*i
        pmt = produto / (juros / juros2)
        print('Cartão 3x Escolhido...\n 20% de Juros\n Parcela x3 de R${:.2f}\n Valor total+juros \033[1;30;43mR${:.2f}\033[m '.format(pmt,pmt*3))

