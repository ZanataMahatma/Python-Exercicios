soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont + 1 # contador a cada ciclo completado o cont vai soma + 1   >> += 1
        soma = soma + c # acumulador a ira somar  tudo dentro da variavel soma   >> += c
print('Somatorio de todos os valores {}  Impares {}'.format(cont,soma))
    
print('fim')