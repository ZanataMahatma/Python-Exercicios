dia = int(input('Quantos dias ele foi alugado ? '))
km = float(input('Quantiade percorridos em KM:'))
preco = 60*dia
rodadokm = km*0.15

print('Preco do carro alugado R${:.2f} por dia \n O valor do KMrodado R${:.2f}\n total a Pagar R${:.2f} '.format(preco,rodadokm,(preco+rodadokm)))
