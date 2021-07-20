#tratamento de erro
''' https://docs.python.org/3/library/exceptions.html '''

try: # tentar
    a =  int(input('Numerador: '))
    b =  int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possivel dividir um número por zero!')
except (KeyboardInterrupt):
    print('O usuario preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado {r:.1f}')

finally: # finalmente
    print('Volte sempre ! Muito Obrigado!.')



'''except Exception as erro: # se der problema
    print(f'Problema encontrado foi {erro.__class__} :(')'''