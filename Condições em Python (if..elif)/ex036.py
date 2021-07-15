'''from time import sleep # importando a tabela TIME para coloca uma simulação de carregamento
casa = float(input('Qual é o valor da casa? :'))
salario = float(input('Digite o Seu Salário: '))
ano = int(input('Quantos anos de financiamento? '))
calc = casa/(ano * 12)
porc = salario * 1.30 - salario
if calc > porc:
    print('Emprestimo negado... seu salario {} excedeu 30%'.format(salario))
else:
    print('Parabêns... vc foi aprovado.PORFAVOR AGUARDE.....')
    sleep(3) # comando para simular um carregamento
    print('O valor da prestação mensal é {:.2f}'.format(calc))
'''

calcular = 'sim'
while calcular == 'sim':
    pagamento =['dinheiro', 'cheque', 'cartão 1x', 'cartão 2x', 'cartão mais que 2x']
    forma = input('Insira sua forma de pagamento:').lower()

    while forma not in pagamento:
        print(f'Esta não é uma forma de pagamento aceita. São aceitas as seguintes formas:{pagamento} \n')
        forma = input('Insira sua forma de pagamento entre uma delas : ').lower()

    preço = (input('Insira o valor em Reais:'))
    while not preço.isdigit():
        preço = (input('Preço deve ser um número. Digite o preço: '))

    preço = float(preço)
    preço = round(preço,2)

    if forma in pagamento[0] or forma in pagamento[1]:
        preço = 0.9 * preço
    elif forma in pagamento[2]:
        preço = 0.95 * preço
    elif forma in pagamento[3]:
        preço = preço
    else:
        preço = 1.2 * preço

    print(f'O preço a pagar é de {preço} considerando pagamento em {forma}')
    calcular = input('Gostaria de calcualar outro preço? sim ou não ').lower()

print('Obrigado por usar nosso sistema. Tenha um bom dia ')