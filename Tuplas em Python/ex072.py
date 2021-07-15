'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida
comuma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
# correção
num = ''
while num != 0: # Desafio  para fica repetindo até sistema ser parado
    tupla2 = ('zero','um','dois','três','quatro'
              ,'cinco','seis','sete','oito','nove',
              'dez','onze','doze','treze','quatorze','quinze'
              ,'dezesseis','dezessete','dezoito','dezenove','vinte')
    while True:
        num = int(input('Digite um numero entre 0 e 20:'))
        if 0 <= num <= 20:
            break
        print('Tente novamente ', end='')
    print(f'Você Digitou o numero:---> {tupla2[num]}')


# minha resposta
'''
tupla = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
tupla2 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input('Digite um número entre 0 e 20:'))
while numero not in tupla:
    numero = int(input('Tente Novamente. Digite um número entre 0 e 20:'))
print(f'Você digitou o número {tupla2[numero]}')'''


