a = [2,3,5,7]
b = a[:] # fatiamento  'a[:]' tira a ligação das 2 lista . removendo esse 'a[:]'   a lista A e B passa a ser uma só
b[2] = 8
print(f'Lista {a}')
print(f'Lista {b}')


valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
print(valores)

#valores = []
#valores.append(5)
#valores.append(2)
#valores.append(8)
#for v in valores:
#   print(f'{v}...',end='')
#for c,v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista.')

'''LISTAS'''
lanche = ['Hamburgue','Suco','Pizza','Picolé'] # lista
lanche.append('Cookies') # Para adicionar itens a lista

# Adicionar na lista na posição q eu desejo.
lanche.insert(0,'Hotdog')# na posição 0

#apagar elementos da LISTA;
del lanche[2] # Deleta pela Posição escolhida
lanche.pop(3) # Deleta pela Posição escolhida     sem o parametro ele Deleta o ultimo iten da lista
lanche.remove('Pizza')# Deleta Pelo valor ou conteudo da lista

#Condição IF para remover Verificar se Cooloes esta na listagem para deletar
if 'Cookies' in lanche:  #O Cookies está no lanche ? ------------ Só vou remover . Se por acaso o Cookies estiver na lista
    lanche.remove('Cookies') #

#Criando uma lista com range.
valores = list(range(4,11)) # Range coloca os valores em ORDEM.. crescente ou decrecente

valores1 = [2,5,6,8,7,9,10]   #exp fora de ordem
valores.sort() # exp Colocando ordem Crescente.
valores.sort(reverse=True) # Colocando em ordem Decrescente.
len(valores1) # Len = Contagem  ele inicia a contagem sem o '0' zero


