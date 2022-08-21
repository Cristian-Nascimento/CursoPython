#Crie um codigo que conte a quantidade de palavreas e caracteres de uma frase

string = "Lorem ipsum dolor sit amet, consectetur adip"
lista_1 = string.split(" ")
lista_2 = string.split(",")

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase. ') #contagem de repetição

print()

#ordenação e contagem de cada elemento da frase
for indice, nome in enumerate(string):
    print(indice, nome)

print()
