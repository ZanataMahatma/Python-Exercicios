peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura**2)
if imc <= 18.5:
    print('Abaixo do Peso. Seu IMC é {:.2f}'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Peso IDEAL!!!. Seu IMC é {:.2f}'.format(imc))
elif imc > 25 and imc <= 30:
    print('Sobrepeso. Seu IMC é {:.2f}'.format(imc))
elif imc > 30 and imc <=40:
    print('Obesidade. Seu IMC é {:.2f}'.format(imc))
else:
    imc > 40
    print('Obesidade Mórbida. Seu IMC atual é {:.2f}'.format(imc))