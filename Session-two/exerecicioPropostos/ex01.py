'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe
se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe
que não é um número inteiro.
'''

teclado = input('insira um número inteiro')

if teclado.isdigit():
    teclado = int(teclado)    

    if (teclado % 2) == 0:
        print(f'o numero {teclado} é par.')
    else:
        print(f'o numero {teclado} é impar.')

else:
    print('favor insira um número inteiro')


#   Ou

#   teclado = input ('insira um número inteiro')

#   if not teclado.isdigit():
#       print('Isso não é um numero inteiro')
#   else:
#       teclado = int(teclado)

#       if not teclado % 2 == 0:
#           print(f'o numero {teclado} é impar.')
#       else:
#           print(f'o numero {teclado} é par.')
