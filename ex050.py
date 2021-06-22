soma = 0
count = 0
for c in range (1,7):
    n = int(input('Digite o numero {}: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        count = count + 1
print('Soma dos numeros pares = {}:'.format(soma))
