"""
Gere uma lista com multiplos de 7, partindo de 0 a 1_000
"""

lista_gerada = list(range(0,1000,7))
print (lista_gerada)

#descobrir o tipo de cada elemento da lista 

lista = ['String', True, 10, -5.18456]

for elem in lista:
     print(f' O tipo de {elem} é {type(elem)}')
