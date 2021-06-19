soma = 0
for c in range (1,7):
    n = int(input('Digite o numero {}: '.format(c)))
    if c % 2:
        soma = soma + n
print('Soma dos numeros pares {}:'.format(soma))
