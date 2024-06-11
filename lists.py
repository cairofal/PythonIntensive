varcafe = ['arara', 'catuai', 'mundo novo', 'gesha', 'conilon'] 

name = 'Cairo'


message = "My coffe crops are mostly composed by" + " " + varcafe[0].title()
print(name)
#print(varcafe[-1].title())
print(message)



varcafe[0] = 'Bourbon'
print(varcafe[0])

varcafe.append('Catuai 2SL')

print(varcafe)

varcafe.insert(0, 'Obatã')
print(varcafe)

del varcafe[0]
print(varcafe)

#O metodo pop() retira o elemento do topo da pilha, ou do final da lista. 
#O valor retirado fica disponivel para ser usado depois de sua retirada.

last_element = varcafe.pop()
message2 = "The last element was" + " " + last_element
print(message2)

#para remover um elemento de qualquer posição da lista, basta apenas incluir um indice
#no metodo pop(), comom por exemplo pop(4).

#metodo remove(): remove um elemento da lista, quando não se sabe sua posição.
varcafe.remove('conilon')
print(varcafe)
#O metodo remove() remove apenas a primeira ocorrencia do valor especificadona lista, 
#Caso haja a possibilidade do valor aparecer mais de uma vez na lista, sera necessario um looping
#para determinar que todas as ocorrencias foram removidas. 

#Método sort() organiza a lista
#Método sort() inverso basta acrescentar lista.sort(reverse=True)
#O metodo sorted() ordena provisoriamente uma lista.

varcafe.sort()
print(varcafe)

#Metodo reverse() reverte a lista de maneira permanente, para voltar, basta usar reverse() novamente
varcafe.reverse()

#o metodo len() permite descobrir o tamanho de uma lista
print(len(varcafe))

#As tuplas se parece com listas, porem, usam parentes no lugar de colchetes
Dimensions = (200,50)

#PEP (Python Enhancement Proposal, ou Proposta de Melhoria de Python)