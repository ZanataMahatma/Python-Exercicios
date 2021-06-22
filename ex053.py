'''Exercício Python 53: Crie um programa que leia uma frase
 qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:'''

frase = str(input('Digite a Frase: ')).strip().upper()
palavras = frase.split() # DEIXA A FRASE EM UMA Lista SEPARA AS PALABRAS
junto = ''.join(palavras) #Subistituio os ESPAÇOS DA PALAVRA << variavel
inverso = junto[::-1] # Comando para ler a frase inverso. fatiamento
'''inverso = ''
for letra in range(len(junto) -1,-1,-1): # len(junto) -1 vai começar da Ultima letro , -1 vai começa a contar antes do 0 , -1 vai voltando uma letra
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALÍndromo')
else:
    print('A frase digitada não é um palíndromo!')

