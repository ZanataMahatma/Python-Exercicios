tupla = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
tupla2 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input('Digite um número entre 0 e 20:'))
while numero not in tupla:
    numero = int(input('Tente Novamente. Digite um número entre 0 e 20:'))
print(f'Você digitou o número {tupla2[numero]}')


