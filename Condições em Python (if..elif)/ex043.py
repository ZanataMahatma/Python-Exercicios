'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite o seu peso kg: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Abaixo do Peso. Seu IMC é {:.1f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Peso IDEAL!!!. Seu IMC é {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('Sobrepeso. Seu IMC é {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade. Seu IMC é {:.1f}'.format(imc))
else:
    imc >= 40
    print('Obesidade Mórbida. Seu IMC atual é {:.1f}'.format(imc))