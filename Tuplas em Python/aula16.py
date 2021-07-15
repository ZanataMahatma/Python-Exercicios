lanche           = ('Hamburguer', 'Suco','Pizza','Pudim','Batata Frita')
print(lanche) # MOSTRA A  TUPLA COMPLETA
print(lanche[1]) # contagem 0,1,2,3  lanche[1] é  =  a SUCO
print(lanche[-2])# contagem -4,-3,-2,-1 lanche[-2] é = a PIZZA
print(lanche[-2:])# contagem -4,-3,-2,-1 lanche[-2:] é  -2 ATÉ O FINAL :  =  PIZZA , pudim.
print(lanche[1:3]) # contagem 0,1,2,3 lanche[1:3] = a SUCO , PIZZA.  1:3 ELEMENTO 3 É IGNORADO.
print(lanche[2:])# contagem 0,1,2,3 lanche[2:] inicia no elemento 2 até o final = PIZZA , PUDIM
print(lanche[:2])# contagem 0,1,2,3 lanche[:2] Me mostre do INICIO até o ELEMENTO 2 = Hamburguer,Suco. ELEMENTO 2 É IGNORADO
# truplas são imutaveis
print('==' * 20)
#forma1
for cont in range (0,len(lanche)):   # cont vai iniciar de  0 a 4 pois o lanche contem essa quantidade de elementos
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')  # vai imprimir lanche de 0 até 4  os elementos da tupla
print('==' * 20)
#forma2
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('==' * 20)
#forma3
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
print('==' * 20)
#forma4
print(sorted(lanche)) # SORTED mostra o lanche em ORDEM ALFABETICA
print('==' * 20)
#forma5
a = (2,5,9)
b = (7,8,4,6,5)
c = a + b
print(c)
print(f'5 está localizado na posição {c.index(5)}')
print(f'Vai contar quantidade total de numeros :{len(c)}')
print(f'Vai verificar a quantidade de numero 5 tem ao total:{c.count(5)}')

