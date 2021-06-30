lanche           = ('Hamburguer', 'Suco','Pizza','Pudim','Batata Frita')
print(lanche) # MOSTRA A  TUPLA COMPLETA
print(lanche[1]) # contagem 0,1,2,3  lanche[1] é  =  a SUCO
print(lanche[-2])# contagem -4,-3,-2,-1 lanche[-2] é = a PIZZA
print(lanche[-2:])# contagem -4,-3,-2,-1 lanche[-2:] é  -2 ATÉ O FINAL :  =  PIZZA , pudim.
print(lanche[1:3]) # contagem 0,1,2,3 lanche[1:3] = a SUCO , PIZZA.  1:3 ELEMENTO 3 É IGNORADO.
print(lanche[2:])# contagem 0,1,2,3 lanche[2:] inicia no elemento 2 até o final = PIZZA , PUDIM
print(lanche[:2])# contagem 0,1,2,3 lanche[:2] Me mostre do INICIO até o ELEMENTO 2 = Hamburguer,Suco. ELEMENTO 2 É IGNORADO
# truplas são imutaveis

for cont in range (0,len(lanche)):   # cont vai iniciar de  0 a 4 pois o lanche contem essa quantidade de elementos
    print(f'Eu vou comer {lanche[cont]}')  # vai imprimir lanche de 0 até 4  os elementos da tupla

'''
print('==' * 20)
for comida in lanche:
    print(f'Eu vou comer {comida}')'''
print('Comi pra caramba')