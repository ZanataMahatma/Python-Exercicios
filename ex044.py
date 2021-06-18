'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
#correção do prof guanabara.

print('{:=^40}'.format('LOJAS ALAVANCAR'))
preço = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc,parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custa R${:.2f} no final.'.format(preço,total))


''' Minha resolução sem correção ..........
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
        print('Cartão 3x Escolhido...\n 20% de Juros\n Parcela x3 de R${:.2f}\n Valor total+juros \033[1;30;43mR${:.2f}\033[m '.format(pmt,pmt*3))'''

