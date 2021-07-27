from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # criar arquivo de text  w = wait  t = tex  + = cria.
        a.close()
    except:
        print('Houce um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criada com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt') # l = leitura de arquivo t = texto
    except:
        print('Erro ao ler ao arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') # o split localiza o ' ; ' que separa e anula do print
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq,nome='desconhecido', idade=0):
    try:
        a= open(arq,'at') # a =  appendind   adicionar  t = arq de texto.
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()