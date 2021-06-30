cédulas = 50
valor = int(input('Qual será o valor a ser sacado? R$'))
total = valor
totalced = 0
while True:
    # Se total for maior igual a cedulas exp valor = 160
    if total >= cédulas:
        total = total - cédulas  #total vai receber total menos a cedulas exp total = 10
        totalced = totalced + 1 # rodou3x   160 - 50 - 50 - 50 = 10
    else: # então se totalced for maior que 0 exp totalced atualmente é igual a 3
        if totalced > 0: # vai imprimir na tela 3x de 50
            print(f'Total de {totalced} cédulas de R${cédulas}')
        if cédulas == 50:# se a cédula for igual a 50
            cédulas = 20 # cédula recebe 20  vai roda   novamente o inicio da WHILE
        elif cédulas == 20:
            cédulas = 10 # cédula recebe 10  vai roda   novamente o inicio da WHILE
        elif cédulas == 10:
            cédulas = 1 # cédula recebe 1  vai roda   novamente o inicio da WHILE
        totalced = 0
        if total == 0:
            break
