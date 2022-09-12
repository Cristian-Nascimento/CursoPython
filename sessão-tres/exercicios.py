'''
Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
'''

def saudacao(saudacao, nome):
    return print(f' {saudacao} {nome}')

saudacao('Faaaala', 'mano')

'''
 Crie uma funcao que recebe 3 numeros como parâmetros e exiba a soma entre eles
'''

def soma(n1,n2,n3):
    return print(n1 + n2 + n3)

soma(4,5,9)

'''
 Crie uma funcao que receba 2 numeros. O primeiro é um valor e o segunda um percentual (ex. 10%). Returne o valor do primeiro número somado
'''

def soma_percentual(valor, percent):
    return print(valor + (valor * percent / 100))

soma_percentual(15,1)
