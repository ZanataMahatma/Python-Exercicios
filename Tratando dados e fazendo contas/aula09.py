'''MANIPULANDO TEXTO'''
'''FRASE: CURSO EM VIDEO PYTHON'''
# len() << comprimento do str
# frase.count(o) << quantidade  de "o"  que tem na suposta frase
# frase.count(o,0,13) <<<< contaria a quantidade de "o" dentro de 0 a 13.  'FATIAMENTO' obg
# ULTIMO NUMERO SEMPRE SERÁ IGNORADO PELO PYTHON DE 0 A 13  >>>  CHEGARA ATE O STR 12
# frase.find('deo')   <<< VAI MOSTRA A POSIÇÃO DOS CARACTERES.
# frase.replace(''python','android'') <<<< Subistitui Palavras da str
# frase.upper() <<<<<<< converter LETRA  MINUSCULAS E MAISCULOS
# frase.lower()  LETRA MAIUSCULAS E MINUSCULAS
# frase.capitalize() CONVERTE TODOS OS CARACTERES EM MINUSCULOS "EXCETO" A PRIMEIRA LETRA DO TEXTO OU FRASE.
# frase.title()  CONVRTE TODAS  AS PRIMEIRAS LETRAS DAS PALAVRAS EM MAISCULAS
# frase.strip() REMOVE TODOS OS ESPAÇOS ESCEDENTE
# frase.rstrip()  "r"  vai remover os ESPAÇOS DO LADO DIREITO
# frase.lstrip() "r"  vai remover os ESPAÇOS DO LADO ESQUERDO

"DIVISÃO"

# frase.split() << cada palavra recebe uma idexação nova de cada STR "GERA UMA LISTA"
# '-'.join(frase) << junta  as palavras utilizando o SEPARADOR >>>  '-' <<<



frase = 'Curso em Vídeo Python'
print(frase[1:15:2])