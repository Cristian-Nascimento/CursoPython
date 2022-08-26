"""
Funções
"""
def funcao_1(bar):
    print(bar)

funcao_1('Valor que eu querer')

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(830,0)

if divide:
    print(f'o resultado da divisao é: {divide}')
else:
    print('Conta invalida')