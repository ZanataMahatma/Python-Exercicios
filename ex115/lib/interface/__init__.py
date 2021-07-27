def leiaInt(msg):
    """

    :param msg: a variavel NUM  envia o comando digitado  para msg.
    :return: Retorna um valor inteiro.
    """
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
            continue  # comando retorna direto pro While até o numero inteiro ser digitado
        except(KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n # comando que retorna para vareavel da função

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu (lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c = c + 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
